#!/usr/bin/env python
from __future__ import annotations

import argparse

from icecube import icetray, dataio
from I3Tray import I3Tray


def count_hit_doms(frame, pulse_key: str, minimum_doms: int) -> bool:
    from icecube import dataclasses

    if pulse_key not in frame:
        return False
    pulses = dataclasses.I3RecoPulseSeriesMap.from_frame(frame, pulse_key)
    hit_doms = sum(1 for _, series in pulses if len(series) > 0)
    frame["TutorialHitDOMs"] = icetray.I3Int(hit_doms)
    return hit_doms >= minimum_doms


def main() -> None:
    parser = argparse.ArgumentParser(description="Select frames with a minimum hit DOM count.")
    parser.add_argument("--gcd", required=True)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--pulse-key", default="SplitInIcePulses")
    parser.add_argument("--minimum-doms", type=int, default=20)
    args = parser.parse_args()

    tray = I3Tray()
    tray.AddModule("I3Reader", "reader", FilenameList=[args.gcd, args.input])
    tray.AddModule(
        count_hit_doms,
        "count_hit_doms",
        pulse_key=args.pulse_key,
        minimum_doms=args.minimum_doms,
        Streams=[icetray.I3Frame.Physics],
    )
    tray.AddModule(
        "I3Writer",
        "writer",
        Filename=args.output,
        Streams=[icetray.I3Frame.TrayInfo, icetray.I3Frame.DAQ, icetray.I3Frame.Physics],
    )
    tray.Execute()
    tray.Finish()


if __name__ == "__main__":
    main()
