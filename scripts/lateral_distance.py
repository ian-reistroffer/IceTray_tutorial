#!/usr/bin/env python
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from icetray_tutorial.frames import event_header_dict, iter_frames, stop_name
from icetray_tutorial.geometry import pulsed_dom_lateral_distances, read_geometry


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Write pulsed DOM lateral distances to a truth track as CSV."
    )
    parser.add_argument("--gcd", required=True)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--pulse-key", default=None)
    parser.add_argument("--truth-key", default=None)
    parser.add_argument("--max-physics-frames", type=int, default=100)
    args = parser.parse_args()

    geometry = read_geometry(args.gcd)
    rows = []
    physics_seen = 0
    for frame in iter_frames(args.input):
        if stop_name(frame) != "Physics":
            continue
        physics_seen += 1
        header = event_header_dict(frame)
        distances = pulsed_dom_lateral_distances(
            frame, geometry, pulse_key=args.pulse_key, truth_key=args.truth_key
        )
        if distances:
            for row in distances:
                rows.append({**header, **row})
        if physics_seen >= args.max_physics_frames:
            break

    with open(args.output, "w", newline="") as fout:
        fieldnames = [
            "run_id",
            "event_id",
            "sub_event_id",
            "sub_event_stream",
            "string",
            "om",
            "truth_key",
            "distance_m",
        ]
        writer = csv.DictWriter(fout, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} DOM-distance rows to {args.output}")


if __name__ == "__main__":
    main()
