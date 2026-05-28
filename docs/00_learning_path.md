# Notebook Overviews

## Notebook 1: Files, Frames, And Keys

`notebooks/01_open_i3_files.ipynb`

An `.i3` file is a stream of frames. A frame is a container of named objects. Each object has a key and a C++/Python type.

To-do's:

- Open a GCD file and an event file with `dataio-shovel`.
- Open the same files in Python with `dataio.I3File`.
- Count frame stops.
- List keys in the first few `Q` and `P` frames.
- Find `I3EventHeader`, `QFilterMask`, pulse maps, and reconstruction keys.

## Notebook 2: Plots From Level2 Files

`notebooks/02_plot_basic_quantities.ipynb`

Convert frame objects into small Python summaries: hit DOM counts, total charge, reconstructed zenith, reconstructed energy-like quantities, and filter pass/fail decisions.

To-do's:

- Build a table with one row per physics frame.
- Plot histograms of hit DOM count and total charge.
- Try several reconstruction keys and see which are present.
- Compare a small simulation sample to a small experimental-data sample.

## Notebook 3: Trays, Modules, And Event Selection

`notebooks/03_trays_modules_filters.ipynb`

Understand the IceTray processing pattern: readers feed frames into a tray; modules inspect or modify frames; writers save selected outputs.

To-do's:

- Build a tray with `I3Reader`.
- Add Python functions as modules.
- Add an `I3ConditionalModule` style class.
- Select events with `QFilterMask`.
- Select events with at least a minimum number of pulsed DOMs.

## Notebook 4: Simulation Truth And Geometry

`notebooks/04_sim_truth_lateral_distance.ipynb`

Understand how the GCD geometry maps OMKeys to DOM positions and how simulation truth can be compared to observed pulses.

To-do's:

- Read `I3Geometry` from the GCD file.
- Keep only in-ice DOMs.
- Identify a simulation truth track candidate, usually `MCPrimary` or another particle key present in the frame.
- Compute the perpendicular distance from each pulsed DOM to the track.
- Plot lateral-distance distributions.

## Notebook 5: HDF5 Output

`notebooks/05_write_hdf5_outputs.ipynb`

Understand that `.i3` is the native event format, while HDF5 is a convenient format for downstream plotting and analysis.

To-do's:

- Write selected IceTray keys with `I3HDFWriter`.
- Write a small custom Pandas table to HDF5 as a lightweight alternative.
- Store outputs under `/data/user/<username>/`, not in the git repository.


