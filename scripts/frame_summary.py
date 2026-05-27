#!/usr/bin/env python
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from icetray_tutorial.frames import count_frame_stops


def main() -> None:
    parser = argparse.ArgumentParser(description="Count frame stops in one or more I3 files.")
    parser.add_argument("files", nargs="+", help="I3 files to inspect")
    parser.add_argument("-n", "--frames", type=int, default=None, help="optional frame limit")
    args = parser.parse_args()

    counts = count_frame_stops(args.files, limit=args.frames)
    for stop, count in counts.most_common():
        print(f"{stop}: {count}")


if __name__ == "__main__":
    main()
