from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Iterable, Iterator


FRAME_STOP_NAMES = {
    "I": "TrayInfo",
    "G": "Geometry",
    "C": "Calibration",
    "D": "DetectorStatus",
    "Q": "DAQ",
    "P": "Physics",
    "S": "Simulation",
    "M": "Mixed",
}
FRAME_STOP_IDS = {name: stop_id for stop_id, name in FRAME_STOP_NAMES.items()}


def _load_dataio():
    try:
        from icecube import dataio
    except ImportError as exc:
        raise RuntimeError(
            "Could not import icecube.dataio. Run this inside an IceTray environment."
        ) from exc
    return dataio


def iter_frames(paths: str | Path | Iterable[str | Path], limit: int | None = None) -> Iterator:
    """Yield frames from one or more I3 files."""
    dataio = _load_dataio()
    if isinstance(paths, (str, Path)):
        paths = [paths]

    yielded = 0
    for path in paths:
        infile = dataio.I3File(str(path))
        try:
            while infile.more():
                frame = infile.pop_frame()
                yield frame
                yielded += 1
                if limit is not None and yielded >= limit:
                    return
        finally:
            infile.close()


def _as_stop_text(value) -> str | None:
    if value is None:
        return None
    if callable(value):
        try:
            value = value()
        except TypeError:
            return None
    if isinstance(value, bytes):
        return value.decode()
    text = str(value)
    if text.startswith("b'") and text.endswith("'"):
        return text[2:-1]
    if text.startswith('b"') and text.endswith('"'):
        return text[2:-1]
    return text


def stop_tokens(frame) -> set[str]:
    """Return all known text forms for a frame stop."""
    if frame is None:
        return set()

    stop = frame.Stop
    tokens = set()
    for value in (stop, getattr(stop, "id", None), getattr(stop, "name", None)):
        text = _as_stop_text(value)
        if text:
            tokens.add(text)
            if text in FRAME_STOP_NAMES:
                tokens.add(FRAME_STOP_NAMES[text])
            if text in FRAME_STOP_IDS:
                tokens.add(FRAME_STOP_IDS[text])
    return tokens


def stop_name(frame) -> str:
    """Return a readable frame stop name."""
    tokens = stop_tokens(frame)
    for stop_id, name in FRAME_STOP_NAMES.items():
        if stop_id in tokens or name in tokens:
            return name
    return next(iter(tokens), "")


def is_stop(frame, *names: str) -> bool:
    """Return True when a frame stop matches any short or long stop name."""
    tokens = stop_tokens(frame)
    requested = set()
    for name in names:
        requested.add(name)
        if name in FRAME_STOP_NAMES:
            requested.add(FRAME_STOP_NAMES[name])
        if name in FRAME_STOP_IDS:
            requested.add(FRAME_STOP_IDS[name])
    return bool(tokens & requested)


def frame_key_table(frame) -> list[dict[str, str]]:
    """Summarize keys and Python-visible object types in one frame."""
    rows = []
    for key in frame.keys():
        try:
            object_type = type(frame[key]).__name__
        except Exception as exc:
            object_type = f"<unreadable: {exc}>"
        rows.append({"key": key, "type": object_type})
    return rows


def count_frame_stops(paths: str | Path | Iterable[str | Path], limit: int | None = None) -> Counter:
    """Count frame stops in one or more files."""
    counts = Counter()
    for frame in iter_frames(paths, limit=limit):
        counts[stop_name(frame)] += 1
    return counts


def first_frame_with_key(paths: str | Path | Iterable[str | Path], key: str, limit: int | None = None):
    """Return the first frame containing a key, or None."""
    for frame in iter_frames(paths, limit=limit):
        if key in frame:
            return frame
    return None


def event_header_dict(frame) -> dict[str, object]:
    """Extract common fields from I3EventHeader when present."""
    if frame is None:
        return {}
    if "I3EventHeader" not in frame:
        return {}
    header = frame["I3EventHeader"]
    fields = [
        "run_id",
        "event_id",
        "sub_event_id",
        "sub_event_stream",
        "start_time",
        "end_time",
    ]
    return {field: getattr(header, field, None) for field in fields}
