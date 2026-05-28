# Environment Notes

## Where To Clone This Repo

Recommended:

```text
/home/<username>/IceTray_tutorial
```

But send large generated files to:

```text
/data/user/<username>/IceTray_tutorial/
```

## Starting An IceTray Environment

In a fresh terminal, type:
```bash
# ssh into your pub.icecube.wisc.edu. This is done automatically if you open a terminal from JupyterHub; otherwise, type:
ssh ireistr@pub.icecube.wisc.edu
# Hop on a Cobalt node:
ssh cobalt
#...enter your password...
# Then type this so your shell can find IceCube software from CVMFS (updates your PATH, PYTHONPATH, LD_LIBRARY_PATH):
eval $(/cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/setup.sh)
# Enter IceTray environment:
/data/user/<username>/<some-icetray-build>/env-shell.sh
```

Now check that Python can import IceCube modules:

```bash
python - <<'PY'
from icecube import icetray, dataio, dataclasses
print("IceTray imports worked")
PY
```

## Opening Files In The Terminal

`dataio-shovel` gets you a human-readable look at an I3 file from a terminal:

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
