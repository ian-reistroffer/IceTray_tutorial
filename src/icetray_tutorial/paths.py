from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


SIM_GCD = Path(
    "/data/exp/IceCube/2020/filtered/level2/0101/Run00133575/"
    "Level2_IC86.2019_data_Run00133575_0101_78_503_GCD.i3.zst"
)
SIM_I3 = Path(
    "/data/sim/IceCube/2020/filtered/level2/CORSIKA-in-ice/20904/"
    "0000000-0000999/Level2_IC86.2020_corsika.020904.000000.i3.zst"
)
EXP_GCD = Path(
    "/data/exp/IceCube/2020/filtered/level2/0101/Run00133576/"
    "Level2_IC86.2019_data_Run00133576_0101_78_503_GCD.i3.zst"
)
EXP_I3 = Path(
    "/data/exp/IceCube/2020/filtered/level2/0101/Run00133576/"
    "Level2_IC86.2019_data_Run00133576_Subrun00000000_00000000.i3.zst"
)


@dataclass(frozen=True)
class FilePair:
    name: str
    gcd: Path
    event_file: Path


SIMULATION = FilePair("simulation", SIM_GCD, SIM_I3)
EXPERIMENT = FilePair("experimental_data", EXP_GCD, EXP_I3)


def data_status() -> list[dict[str, str | bool]]:
    """Return whether the tutorial's default data files exist locally."""
    rows = []
    for label, path in [
        ("simulation_gcd", SIM_GCD),
        ("simulation_i3", SIM_I3),
        ("experimental_gcd", EXP_GCD),
        ("experimental_i3", EXP_I3),
    ]:
        rows.append({"label": label, "path": str(path), "exists": path.exists()})
    return rows
