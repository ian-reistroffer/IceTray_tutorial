from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Iterable, Iterator


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


def stop_name(frame) -> str:
    """Return a readable frame stop name."""
    stop = frame.Stop
    return getattr(stop, "id", str(stop))


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
