# I3 Files And Frames

IceTray processes IceCube data as a stream of frames. A frame is a named-object container. Every object in the frame has a key, and modules communicate by reading and writing those keys.

## Common Frame Stops

`I` / TrayInfo: processing history and provenance. You usually inspect this but do not analyze it event-by-event.

`G` / Geometry: detector geometry. For this tutorial, the most important object is `I3Geometry`, which maps each in-ice OMKey to a DOM position.

`C` / Calibration: calibration constants used to interpret DOM waveforms and pulses.

`D` / DetectorStatus: run-specific detector configuration, such as which DOMs were active and which triggers and filters were configured.

`Q` / DAQ: event-level readout before split-event processing. This is the natural place to find trigger and raw event information.

`P` / Physics: processed event information, usually after event splitting. Level2 files often store reconstructed particles, pulse maps, filter results, and analysis-ready quantities in `P` frames.

## GCD Files

GCD means Geometry, Calibration, and DetectorStatus. Use the GCD file matched to the run or simulation set. The notebooks load the GCD first when geometry or detector configuration is needed.

## Simulation Versus Experimental Data

Experimental Level2 data generally contains detector readout, filters, cleaned pulses, and reconstruction results. It does not contain Monte Carlo truth.

Simulation Level2 data often contains all of the above plus truth information, for example `I3MCTree`, `MCPrimary`, weight dictionaries, or other simulation objects. Exact keys vary by production.

## InIce Scope

This repository intentionally ignores IceTop. In helper code, in-ice DOMs are treated as OMKeys with IceCube strings and DOM numbers in the in-ice range. If you inspect files with IceTop keys, treat them as out of scope for these lessons.
