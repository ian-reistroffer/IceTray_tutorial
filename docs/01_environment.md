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
# (use your own username)

# Hop on a Cobalt node:
ssh cobalt
#...enter your password...

# Then type this so your shell can find IceCube software from CVMFS (updates your PATH, PYTHONPATH, LD_LIBRARY_PATH):
eval $(/cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/setup.sh)

# Enter IceTray environment:
eval /home/ireistr/i3/icetray/build/env-shell.sh
# (this should be usable; eventually you'll build your own)
```

If all has gone right, you should see something like this:

```
************************************************************************
*                                                                      *
*                   W E L C O M E  to  I C E T R A Y                   *
*                                                                      *
*                Version icetray.main     git:80859e2d                 *
*                                                                      *
*                You are welcome to visit our Web site                 *
*                        http://icecube.umd.edu                        *
*                                                                      *
************************************************************************

Icetray environment has:
   I3_SRC       = /home/ireistr/i3/icetray/src
   I3_BUILD     = /home/ireistr/i3/icetray/build
   I3_TESTDATA  = /cvmfs/icecube.opensciencegrid.org/py3-v4.3.0/../data/i3-test-data-svn/trunk
   I3_PRODDATA should be set to an existing directory path
   Python       = 3.11.3
```

Now check that Python can import IceCube modules:

```bash
python - <<'PY'
from icecube import icetray, dataio, dataclasses
print("IceTray imports worked")
PY
```

## Opening Files In The Terminal

`dataio-shovel` gets you a human-readable look at an I3 file from a terminal. For example:

```bash
dataio-shovel /data/exp/IceCube/2020/filtered/level2/0101/Run00133576/Level2_IC86.2019_data_Run00133576_Subrun00000000_00000000.i3.zst
```

Or, to see GCD frames at the front, simply add a path to the right GCD:


```bash
dataio-shovel /data/exp/IceCube/2020/filtered/level2/0101/Run00133576/Level2_IC86.2019_data_Run00133576_0101_78_503_GCD.i3.zst /data/exp/IceCube/2020/filtered/level2/0101/Run00133576/Level2_IC86.2019_data_Run00133576_Subrun00000000_00000000.i3.zst
```

This should work with any .i3 file.

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

## Notebook Environments

Similar to entering the IceTray environment in a Termninal, to use IceTray software in a notebook you must select the right notebook kernel.

After opening a notebook, select "Kernel" -> "Change Kernel..." -> In the drop-down menu, select the desired kernel. Usually the most up-to-date python kernel, e.g., "py3-v4.3.0: v1.12.1".
