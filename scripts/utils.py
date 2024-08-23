import argparse
import re
from pathlib import Path


def validate_version(version):
    # Regular expression to match X.X.X where X are numbers
    pattern = re.compile(r"^\d+\.\d+\.\d+$")
    if not pattern.match(version):
        raise argparse.ArgumentTypeError(
            f"Invalid version format: '{version}'. Expected format: 'X.X.X' where X are numbers."
        )
    return version


def list_folders_in_path(path: Path) -> list[Path]:
    return [x for x in path.glob("*") if x.is_dir()]


def require_tag_from_cli() -> str:
    parser = argparse.ArgumentParser(
        description="Process a version number in the format X.X.X"
    )
    parser.add_argument(
        "version", type=validate_version, help="The version number in the format X.X.X"
    )
    args = parser.parse_args()
    return f"{args.version}"
