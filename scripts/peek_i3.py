#!/usr/bin/env python
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from icetray_tutorial.frames import event_header_dict, frame_key_table, iter_frames, stop_name


def main() -> None:
    parser = argparse.ArgumentParser(description="Print keys from the first few I3 frames.")
    parser.add_argument("files", nargs="+", help="I3 files to inspect")
    parser.add_argument("-n", "--frames", type=int, default=5, help="maximum frames to print")
    args = parser.parse_args()

    for index, frame in enumerate(iter_frames(args.files, limit=args.frames), start=1):
        print(f"\nFrame {index}: {stop_name(frame)}")
        header = event_header_dict(frame)
        if header:
            print("  event:", header)
        for row in frame_key_table(frame):
            print(f"  {row['key']:<45} {row['type']}")


if __name__ == "__main__":
    main()
