import argparse
import re
from pathlib import Path

CURRENT_DIR: Path = Path(__file__).resolve().parent

_TEMPLATE: str = """Click on the link for a list of all the PRs released since `{version_tag}` 
https://github.com/ITISFoundation/osparc-simcore/compare/{version_tag}...master

**Draft release notes go below the line**
---
"""


def _validate_version(version):
    # Regular expression to match X.X.X where X are numbers
    pattern = re.compile(r"^\d+\.\d+\.\d+$")
    if not pattern.match(version):
        raise argparse.ArgumentTypeError(
            f"Invalid version format: '{version}'. Expected format: 'X.X.X' where X are numbers."
        )
    return version


def _list_folders_in_path(path: Path) -> list[Path]:
    return [x for x in path.glob("*") if x.is_dir()]


def _get_previous_version(vtag: str) -> int:
    version_parts = vtag.strip("v").split(".")
    version_parts[1] = f"{int(version_parts[1])-1}"

    return "v" + ".".join(version_parts)


def main():
    parser = argparse.ArgumentParser(
        description="Process a version number in the format X.X.X"
    )
    parser.add_argument(
        "version", type=_validate_version, help="The version number in the format X.X.X"
    )
    args = parser.parse_args()

    tag = f"v{args.version}"

    print(f"Will generate form tag: {tag}")

    new_draft_content = _TEMPLATE.format(version_tag=_get_previous_version(tag))
    for product_folder in _list_folders_in_path(CURRENT_DIR / ".." / "release-notes"):
        draft_file = product_folder / f"{tag}.md"
        if draft_file.exists():
            msg = f"{draft_file} already exists, make sure you are creating the draft for the correct release"
            raise ValueError(msg)
        draft_file.write_text(new_draft_content)


if __name__ == "__main__":
    main()
