from __future__ import annotations

from dataclasses import dataclass


PULSE_KEY_CANDIDATES = (
    "SplitInIcePulses",
    "SplitInIceDSTPulses",
    "SRTInIcePulses",
    "InIcePulses",
    "OfflinePulses",
    "CleanedMuonPulses",
)


@dataclass(frozen=True)
class PulseSummary:
    pulse_key: str
    hit_doms: int
    pulses: int
    total_charge: float


def _load_dataclasses():
    try:
        from icecube import dataclasses
    except ImportError as exc:
        raise RuntimeError(
            "Could not import icecube.dataclasses. Run this inside an IceTray environment."
        ) from exc
    return dataclasses


def find_pulse_key(frame, candidates: tuple[str, ...] = PULSE_KEY_CANDIDATES) -> str | None:
    """Return the first known pulse key present in a frame."""
    for key in candidates:
        if key in frame:
            return key
    return None


def pulse_series_from_frame(frame, pulse_key: str | None = None):
    """Read an I3RecoPulseSeriesMap, handling common map-mask cases."""
    dataclasses = _load_dataclasses()
    key = pulse_key or find_pulse_key(frame)
    if key is None:
        raise KeyError("No known in-ice pulse key found in this frame.")
    return key, dataclasses.I3RecoPulseSeriesMap.from_frame(frame, key)


def summarize_pulses(frame, pulse_key: str | None = None) -> PulseSummary | None:
    """Count hit DOMs, pulses, and total charge for a pulse map."""
    key = pulse_key or find_pulse_key(frame)
    if key is None:
        return None
    _, pulse_map = pulse_series_from_frame(frame, key)

    hit_doms = 0
    pulse_count = 0
    total_charge = 0.0
    for _, series in pulse_map:
        hit_doms += 1
        pulse_count += len(series)
        total_charge += sum(float(p.charge) for p in series)

    return PulseSummary(key, hit_doms, pulse_count, total_charge)


def hit_omkeys(frame, pulse_key: str | None = None):
    """Return OMKeys that have at least one pulse."""
    _, pulse_map = pulse_series_from_frame(frame, pulse_key)
    return [omkey for omkey, series in pulse_map if len(series) > 0]
