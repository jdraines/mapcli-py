from pathlib import Path
import sys
from pathlib import Path
import yaml
import subprocess
from logging import getLogger


logger = getLogger(__name__)


def map_argv(map: dict[str, str], argv: list[str]):
    logger.debug(f"argv: {argv}")
    args = []
    for i, a in enumerate(argv):
        if not i and Path(a).exists:
            a = Path(a).name
        if a in map:
            args.append(map[a])
        else:
            args.append(a)
    return args


def load_map(path: Path):
    with open(path, "rt") as f:
        return yaml.safe_load(f)


def map_command(map_path: Path):
    map = load_map(map_path)
    logger.debug(f"Map loaded: {map}")
    mapped_cmd = map_argv(map, sys.argv)
    subprocess.run(mapped_cmd)
