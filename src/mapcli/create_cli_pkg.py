from pathlib import Path
from argparse import ArgumentParser
import sys

from copier import run_copy


template_dir = Path(__file__).parent / "templates" / "pyproject"
default_destination_parent = Path("~/mapcli").expanduser()


def create_cli(destination_dir: Path, data: dict[str, str]):
    run_copy(str(template_dir), str(destination_dir), data=data)


def get_args():
    parser = ArgumentParser()
    parser.add_argument("new_cli_name")
    parser.add_argument("--destination", "-o", required=False)
    args = parser.parse_args()
    if not args.destination:
        args.destination = default_destination_parent / args.new_cli_name
    return args


def main():
    args = get_args()
    py_v = sys.version_info
    python_version = f"{py_v[0]}.{py_v[1]}"
    data = {"new_cli_name": args.new_cli_name, "python_version": python_version}
    create_cli(args.destination, data)
