#!/usr/bin/env python
from __future__ import annotations

import argparse

from icecube import dataio
from I3Tray import I3Tray


def main() -> None:
    parser = argparse.ArgumentParser(description="Write selected IceTray keys to HDF5.")
    parser.add_argument("--gcd", required=True)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--keys",
        nargs="+",
        default=["I3EventHeader", "QFilterMask"],
        help="Frame keys to write",
    )
    parser.add_argument(
        "--sub-event-streams",
        nargs="+",
        default=["InIceSplit"],
        help="Physics sub-event streams to write",
    )
    args = parser.parse_args()

    from icecube.hdfwriter import I3HDFWriter

    tray = I3Tray()
    tray.AddModule("I3Reader", "reader", FilenameList=[args.gcd, args.input])
    tray.AddSegment(
        I3HDFWriter,
        "hdf",
        Output=args.output,
        Keys=args.keys,
        SubEventStreams=args.sub_event_streams,
    )
    tray.Execute()
    tray.Finish()


if __name__ == "__main__":
    main()
