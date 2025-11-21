from mapcli import map_command
from pathlib import Path

map_path = Path(__file__).parent.parent.parent / "map.yaml"


def main():
    map_command(map_path)
