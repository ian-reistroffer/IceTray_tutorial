# IceTray Tutorial: InIce Cosmic-Ray Analysis

This is an introduction to the IceTray software framework used in IceCube analyses.

It focuses on the in-ice detector only: DOMs on IceCube strings, event frames, pulse series, filters, reconstructed quantities, simulation truth, and small analysis outputs.

The main tutorial code is copied inside the notebooks: file paths, loops, functions, etc. The `src/` package and `scripts/` directory are references to put all those things in one place; they're not required to execute any code in the notebooks.

## Main Take-Aways:

1. Open `.i3` and `.i3.zst` files with `dataio-shovel` and Python.
2. Review the frame model: `I`, `G`, `C`, `D`, `Q`, and `P` frames.
3. Inspect frame keys and common IceCube object types.
4. Read pulse maps, count hit DOMs, plot in-ice event quantities.
5. Use `QFilterMask` to select events that passed certain filters.
6. Build IceTray trays, modules, and conditional processing functions.
7. Compare pulsed DOM locations to simulation truth tracks.
8. Write selected frame quantities to HDF5 for later analysis.

## Quick Start On JupyterHub

Clone the repository into your home directory:

```bash
cd ~
git clone https://github.com/ian-reistroffer/IceTray_tutorial.git
cd IceTray_tutorial
```

If that doesn't work, do this instead:

```bash

```

Enter an IceTray environment. The exact metaproject changes over time, but a typical CVMFS pattern is:

```bash
eval `/cvmfs/icecube.opensciencegrid.org/py3-v4.4.0/setup.sh`
icetray-shell
```

Then open the notebooks:

```bash
jupyter lab
```

## Example Files Used Throughout

Simulation:

```text
GCD: /data/exp/IceCube/2020/filtered/level2/0101/Run00133575/Level2_IC86.2019_data_Run00133575_0101_78_503_GCD.i3.zst
I3:  /data/sim/IceCube/2020/filtered/level2/CORSIKA-in-ice/20904/0000000-0000999/Level2_IC86.2020_corsika.020904.000000.i3.zst
```

Experimental data:

```text
GCD: /data/exp/IceCube/2020/filtered/level2/0101/Run00133576/Level2_IC86.2019_data_Run00133576_0101_78_503_GCD.i3.zst
I3:  /data/exp/IceCube/2020/filtered/level2/0101/Run00133576/Level2_IC86.2019_data_Run00133576_Subrun00000000_00000000.i3.zst
```

The notebooks read only a limited number of frames by default so they remain interactive. Large outputs should go under your `/data/user/<username>/` directory.

## Repository Layout

```text
docs/
  00_learning_path.md        Suggested course sequence
  01_environment.md          Madison/JupyterHub setup notes
  02_i3_files_and_frames.md  Conceptual guide to files and frames
  03_inice_analysis_notes.md InIce-specific analysis reminders
notebooks/
  01_open_i3_files.ipynb
  02_plot_basic_quantities.ipynb
  03_trays_modules_filters.ipynb
  04_sim_truth_lateral_distance.ipynb
  05_write_hdf5_outputs.ipynb
scripts/
  peek_i3.py
  frame_summary.py
  dom_count_tray.py
  lateral_distance.py
  export_hdf5.py
src/icetray_tutorial/
  paths.py
  frames.py
  pulses.py
  filters.py
  geometry.py
```

## Suggested Order

1. Read `docs/00_learning_path.md`.
2. Run `notebooks/01_open_i3_files.ipynb`.
3. Use `dataio-shovel` on both the GCD file and event file.
4. Run `notebooks/02_plot_basic_quantities.ipynb`.
5. Run `notebooks/03_trays_modules_filters.ipynb`.
6. Run `notebooks/04_sim_truth_lateral_distance.ipynb`.
7. Finish with `notebooks/05_write_hdf5_outputs.ipynb`.

## Useful External References

- IceCube docs landing page: <https://docs.icecube.aq/>
- IceTray tutorial slides, including frame and `dataio-shovel` overview:
  <https://events.icecube.wisc.edu/event/313/contributions/11144/attachments/8456/11231/IceTray%20Tutorial.pdf>
- IceTray `I3Module` reference:
  <https://user-web.icecube.wisc.edu/~jvansanten/icerec-dev-docs/projects/icetray/i3module.html>
- IceCube dataclasses reference:
  <https://user-web.icecube.wisc.edu/~jvansanten/icerec-dev-docs/projects/dataclasses/index.html>
