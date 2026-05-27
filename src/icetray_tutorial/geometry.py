from __future__ import annotations

from math import cos, sin
from pathlib import Path

import numpy as np

from .frames import is_stop, iter_frames
from .pulses import hit_omkeys

TRUTH_KEY_CANDIDATES = (
    "MCPrimary",
    "MostEnergeticMuon",
    "MostEnergeticInIceMuon",
    "MCMuon",
    "PolyplopiaPrimary",
)


def read_geometry(gcd_file: str | Path):
    """Return I3Geometry from the first geometry frame in a GCD file."""
    for frame in iter_frames(gcd_file):
        if is_stop(frame, "Geometry") and "I3Geometry" in frame:
            return frame["I3Geometry"]
    raise KeyError(f"No I3Geometry found in {gcd_file}")


def is_inice_omkey(omkey) -> bool:
    """Keep standard in-ice IceCube DOMs and reject IceTop-style OMKeys."""
    return 1 <= int(omkey.string) <= 86 and 1 <= int(omkey.om) <= 60


def dom_position(geometry, omkey) -> np.ndarray:
    """Return DOM position as an x, y, z numpy vector."""
    pos = geometry.omgeo[omkey].position
    return np.array([float(pos.x), float(pos.y), float(pos.z)])


def inice_dom_positions(geometry) -> dict[object, np.ndarray]:
    """Return positions for all in-ice DOMs in the geometry."""
    return {
        omkey: dom_position(geometry, omkey)
        for omkey in geometry.omgeo.keys()
        if is_inice_omkey(omkey)
    }


def particle_position(particle) -> np.ndarray:
    pos = particle.pos
    return np.array([float(pos.x), float(pos.y), float(pos.z)])


def particle_direction(particle) -> np.ndarray:
    direction = particle.dir
    if all(hasattr(direction, attr) for attr in ("x", "y", "z")):
        vec = np.array([float(direction.x), float(direction.y), float(direction.z)])
    else:
        zenith = float(direction.zenith)
        azimuth = float(direction.azimuth)
        vec = np.array(
            [
                sin(zenith) * cos(azimuth),
                sin(zenith) * sin(azimuth),
                cos(zenith),
            ]
        )
    norm = np.linalg.norm(vec)
    if norm == 0:
        raise ValueError("Particle direction vector has zero length.")
    return vec / norm


def distance_point_to_track(point: np.ndarray, particle) -> float:
    """Perpendicular distance from a point to an I3Particle track line."""
    origin = particle_position(particle)
    unit_direction = particle_direction(particle)
    return float(np.linalg.norm(np.cross(point - origin, unit_direction)))


def is_particle_like(obj) -> bool:
    """Return True for objects that look enough like an I3Particle track."""
    return hasattr(obj, "pos") and hasattr(obj, "dir")


def particle_like_keys(frame, words: tuple[str, ...] = ("mc", "truth", "primary", "muon")) -> list[str]:
    """Return frame keys that look like truth-track particle objects."""
    keys = []
    for key in frame.keys():
        if not any(word in key.lower() for word in words):
            continue
        try:
            obj = frame[key]
        except Exception:
            continue
        if is_particle_like(obj):
            keys.append(key)
    return keys


def find_truth_track(frame, candidates: tuple[str, ...] = TRUTH_KEY_CANDIDATES):
    """Return the first available truth-track-like particle from a frame."""
    for key in candidates:
        if key in frame and is_particle_like(frame[key]):
            return key, frame[key]
    for key in particle_like_keys(frame):
        return key, frame[key]
    return None, None


def pulsed_dom_lateral_distances(frame, geometry, pulse_key: str | None = None, truth_key: str | None = None):
    """Compute lateral distances from pulsed in-ice DOMs to a truth track."""
    if truth_key:
        if truth_key not in frame:
            raise KeyError(f"{truth_key} not found in frame")
        track_key, track = truth_key, frame[truth_key]
    else:
        track_key, track = find_truth_track(frame)
    if track is None:
        return None

    rows = []
    for omkey in hit_omkeys(frame, pulse_key):
        if not is_inice_omkey(omkey):
            continue
        try:
            position = dom_position(geometry, omkey)
        except Exception:
            continue
        rows.append(
            {
                "string": int(omkey.string),
                "om": int(omkey.om),
                "truth_key": track_key,
                "distance_m": distance_point_to_track(position, track),
            }
        )
    return rows
