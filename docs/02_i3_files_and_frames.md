# I3 Files And Frames

IceTray processes IceCube data as a stream of frames. A frame is a named-object container. Every object in the frame has a key, and modules communicate by reading and writing those keys.

## Common Frame "Stops"

`I` / TrayInfo: processing history and provenance. You can inspect this but the information is mostly bookkeeping.

`G` / Geometry: detector geometry. For us, the most important object in a G-frame is `I3Geometry`. This maps each in-ice OMKey to a DOM position.

`C` / Calibration: calibration constants used to interpret DOM waveforms and pulses.

`D` / DetectorStatus: run-specific detector configuration, such as which DOMs were active and which triggers and filters were configured.

`Q` / DAQ: event-level readout before split-event processing. This is the place to find trigger and raw event information.

`P` / Physics: processed event information, after event splitting. Level2 files can store reconstructed particles, pulse maps, filter results, and other analysis quantities in `P` frames.


## GCD Files

GCD means Geometry, Calibration, and DetectorStatus. Use the GCD file matched to the run or simulation set. The notebooks load the GCD first when geometry or detector configuration is needed.

## Simulation Versus Experimental Data

Experimental Level2 data generally contains detector readout, filters, cleaned pulses, and reconstruction results. It does not contain Monte Carlo truth.

Simulation Level2 data often contains all of the above plus truth information, for example `I3MCTree`, `MCPrimary`, weight dictionaries, or other simulation objects. Exact keys vary by production.
