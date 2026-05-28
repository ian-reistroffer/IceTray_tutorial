# Miscellaneous Analysis Notes

- Level2 files can be huge. Read 100 or 1000 physics frames first, make sure the logic works, then scale up.
- Different files and processing versions use different key names.
  - I put helper functions in the notebooks look for common pulse and reconstruction names so that different data files may be tested in the future, but it's better practice to print the frame keys to see if a wanted key exists.

## Pulse Maps And Masks

Pulse keys may store either an `I3RecoPulseSeriesMap` or a mask that points to one. Use:

```python
from icecube import dataclasses
pulses = dataclasses.I3RecoPulseSeriesMap.from_frame(frame, pulse_key)
```

That should work for common pulse maps and masks.

## Filter Results

`QFilterMask` stores named filter decisions. A filter is normally considered passed when both `condition_passed` and `prescale_passed` are true.

## Reconstruction Keys

There's no single universal reconstruction key in every file. Common particle or energy-related keys can include names containing:

```text
SplineMPE
MPEFit
LineFit
MuEX
Millipede
OnlineL2
```

Print available keys, inspect their types, and then choose the most relevant one for the exercise.

## Simulation Truth

For CORSIKA in-ice simulation, `MCPrimary` or `PolyplopiaPrimary` is the truth particle.
