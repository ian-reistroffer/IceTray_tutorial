# Learning Path

This tutorial is designed as a short, practical introduction rather than a complete IceTray course. The goal is to help a student become comfortable opening files, understanding frames, extracting useful quantities, and writing small IceTray analyses for in-ice cosmic-ray work.

## Lesson 1: Files, Frames, And Keys

Start with `notebooks/01_open_i3_files.ipynb`.

Students should learn that an `.i3` file is a stream of frames. A frame is a container of named objects. Each object has a key and a C++/Python type.

Practice goals:

- Open a GCD file and an event file with `dataio-shovel`.
- Open the same files in Python with `dataio.I3File`.
- Count frame stops.
- List keys in the first few `Q` and `P` frames.
- Find `I3EventHeader`, `QFilterMask`, pulse maps, and reconstruction keys.

## Lesson 2: Basic Plots From Level2 Files

Continue with `notebooks/02_plot_basic_quantities.ipynb`.

Students should learn to convert frame objects into small Python summaries: hit DOM counts, total charge, reconstructed zenith, reconstructed energy-like quantities, and filter pass/fail decisions.

Practice goals:

- Build a table with one row per physics frame.
- Plot histograms of hit DOM count and total charge.
- Try several reconstruction keys and see which are present.
- Compare a small simulation sample to a small experimental-data sample.

## Lesson 3: Trays, Modules, And Event Selection

Continue with `notebooks/03_trays_modules_filters.ipynb`.

Students should learn the IceTray processing pattern: readers feed frames into a tray; modules inspect or modify frames; writers save selected outputs.

Practice goals:

- Build a tray with `I3Reader`.
- Add Python functions as modules.
- Add an `I3ConditionalModule` style class.
- Select events with `QFilterMask`.
- Select events with at least a minimum number of pulsed DOMs.

## Lesson 4: Simulation Truth And Geometry

Continue with `notebooks/04_sim_truth_lateral_distance.ipynb`.

Students should learn how the GCD geometry maps OMKeys to DOM positions and how simulation truth can be compared to observed pulses.

Practice goals:

- Read `I3Geometry` from the GCD file.
- Keep only in-ice DOMs.
- Identify a simulation truth track candidate, usually `MCPrimary` or another particle key present in the frame.
- Compute the perpendicular distance from each pulsed DOM to the track.
- Plot lateral-distance distributions.

## Lesson 5: HDF5 Output

Finish with `notebooks/05_write_hdf5_outputs.ipynb`.

Students should learn that `.i3` is the native event format, while HDF5 is a convenient format for downstream plotting and analysis.

Practice goals:

- Write selected IceTray keys with `I3HDFWriter`.
- Write a small custom Pandas table to HDF5 as a lightweight alternative.
- Store outputs under `/data/user/<username>/`, not in the git repository.

## Capstone Exercises

Choose one:

1. Make a filter-comparison table for the experimental file. Which named filters appear in `QFilterMask`, and what fraction of inspected events pass?
2. For simulation, plot lateral distance from the truth track for events with at least 20 hit DOMs.
3. Write an HDF5 file containing `I3EventHeader`, one reconstructed particle, `QFilterMask`, and custom hit statistics.
4. Build a small command-line script that prints one line per event: run, event, subevent stream, hit DOM count, total charge, selected filters.
