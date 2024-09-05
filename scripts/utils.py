import argparse
import re
from pathlib import Path

INITIALS_TO_USERNAMES: dict[str, str] = {
    "ANE": "GitHK",
    "BL": "dyollb",
    "DK": "mrnicegyu11",
    "EI": "elisabettai",
    "IP": "ignapas",
    "GCR": "giancarloromeo",
    "MaG": "mguidon",
    "JQU": "jsaq007",
    "MB": "bisgaard-itis",
    "MD": "matusdrobuliak66",
    "MEST": "Konohana0608",
    "OM": "odeimaiz",
    "PC": "pcrespov",
    "SAN": "sanderegg",
    "SB": "sbenkler",
    "SCA": "SCA-ZMT",
    "TN": "newton1985",
    "WVG": "wvangeit",
    "YH": "YuryHrytsuk",
}


def validate_date(date_str: str) -> str:
    pattern = re.compile(r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])$")
    if not pattern.match(date_str):
        raise argparse.ArgumentTypeError(
            f"Invalid date format: '{date_str}'. Expected format: 'dd.mm' where dd is a valid day and mm is a valid month"
        )
    return date_str


def validate_time(date_str: str) -> str:
    pattern = re.compile(r"^(?:[01][0-9]|2[0-3]):[0-5][0-9]$")
    if not pattern.match(date_str):
        raise argparse.ArgumentTypeError(
            f"Invalid date format: '{date_str}'. Expected format: 'HH:MM' where HH is a valid hour and MM is a valid minute"
        )
    return date_str


def validate_version(version):
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
