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

GCD means Geometry, Calibration, and DetectorStatus. Use the GCD file matched to the run or simulation set.

## Simulation Versus Experimental Data

Experimental Level2 data generally contains detector readout, filters, cleaned pulses, and reconstruction results. It does not contain Monte Carlo truth.

Simulation Level2 data often contains all of the above plus truth information, for example `I3MCTree`, `MCPrimary`, weight dictionaries, or other simulation objects. Exact keys vary by production.

## Processing "Levels"

(copied from https://wiki.icecube.wisc.edu/index.php/Newbies)

From IceCube, data is filtered by **levels**.

The raw data coming directly from the Pole via satellite is **Level 0**. Then, several programs are run to get to **Level 1** and **Level 2**, etc.

Higher levels $=$ more filtering has been done, and the more advanced parameters are in the frames. The raw data parameters are mostly gone by the time you get to higher levels.

However, no events are deleted at the lower levels (only at **Level 3** and above).

---

There are various levels with differing purposes:

**Level 0**: Triggering the detector (often simply called "**trigger-level**").  
This is very fast and aims to separate "maybe interesting" (any particle interaction) from "definitely not interesting" (noise in the detector) by looking at the number of hits in the detector as a function of time.

**Level 1**: Filtering (often called "**filter-level**").  
Here, we have a rate of ~3 kHz which is primarily dominated by atmospheric muons. For comparison, atmospheric neutrino rates are on the order of 10-20 mHz. To reduce the background rates, we specialize our data into different filters with varying energy and topology goals.
- For example, the <u>muon filter</u> looks for muons that pass through the full detector >1 TeV, while the <u>DeepCore filter</u> looks for events  <100 GeV interacting in the bottom of the detector.

**Level 2**: Collaboration-wide processing.  
Here, we are not trying to remove events, but are rather **applying reconstructions** and processing for each filter. No events get removed during the L2 processing.

**Level 3**: Working-group specific processing.  
The three main L3 chains (cascades, muons, and low energy) cut on the events passing a subset of filters, then apply new reconstructions to reduce rates further. These get rates below about 1 Hz.

**Level 4+**: Event-selection specific processing.  
These are additional stages of processing used to get from the ~1 Hz L3 rates down to a neutrino-dominated sample. The number of additional levels depends on the analyzer and isn't terribly meaningful by itself.
