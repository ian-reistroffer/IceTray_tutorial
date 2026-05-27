# Environment Notes

IceTray is normally used from an IceCube software environment. This repository does not vendor IceTray, detector data, or large simulation files.

## Where To Work

Recommended:

```text
/home/<username>/IceTray_tutorial
```

Large generated files:

```text
/data/user/<username>/IceTray_tutorial/
```

Avoid committing generated `.i3`, `.i3.zst`, `.hdf5`, `.h5`, or large plot directories.

## Starting An IceTray Environment

Your exact command may depend on the metaproject version used by your group. A common pattern is:

```bash
eval `/cvmfs/icecube.opensciencegrid.org/py3-v4.4.0/setup.sh`
icetray-shell
```

Some courses or analysis groups provide a built IceTray checkout:

```bash
/data/user/<username>/<some-icetray-build>/env-shell.sh
```

Inside the shell, check that Python can import IceCube modules:

```bash
python - <<'PY'
from icecube import icetray, dataio, dataclasses
print("IceTray imports worked")
PY
```

## Opening Files In The Terminal

`dataio-shovel` is the fastest way to get a human-readable first look at an I3 file from a terminal:

```bash
dataio-shovel /data/exp/IceCube/2020/filtered/level2/0101/Run00133576/Level2_IC86.2019_data_Run00133576_0101_78_503_GCD.i3.zst /data/exp/IceCube/2020/filtered/level2/0101/Run00133576/Level2_IC86.2019_data_Run00133576_Subrun00000000_00000000.i3.zst
```

Useful `dataio-shovel` keys:

```text
enter  open the selected object
q      go back or quit
?      show help
g      go to a frame number
e      go to an event number
{      first frame
}      last frame
i      interactive Python shell
L      load a library
```

## Notebook Imports

Each notebook adds `../src` to `sys.path`, so the helper package can be used without installation. If you prefer an editable install:

```bash
python -m pip install -e .
```
