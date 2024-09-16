import argparse
from pathlib import Path

from utils import (
    INITIALS_TO_USERNAMES,
    list_folders_in_path,
    validate_date,
    validate_time,
    validate_version,
)

CURRENT_DIR: Path = Path(__file__).resolve().parent

INITIALS: list[str] = list(INITIALS_TO_USERNAMES.keys())

_TEMPLATE: str = """Click on the link for a list of all the PRs released since `{version_tag}`
https://github.com/ITISFoundation/osparc-simcore/compare/{version_tag}...master

Please check your name if finished:
{names_to_check}

**Draft release notes go below the line**
---
# Release Notes
### Highlights
"""


_MATTERMOST_TEMPLATE: str = """
@all please contribute in compiling the `Release Drafts`.
There are 3 release drafts to fill out: `s4l` (which also includes s4li-lite), `osparc`, `tip`.
Instructions:
- Please go through all your last changes in master since the last release for each product: [osparc](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/osparc/{version_tag}.md), [s4l](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/{version_tag}.md) and [tip](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/tip/{version_tag}.md) (each product contains a link to these changes)
- For each product please chose those features which it makes sense to highlight.
- When highlighting a feature please provide a meaningful `USER` readable description and the link to the PR
- deadline `{deadline_day} by {deadline_time}`
- please :white_check_mark: your name when done in all products so I can keep track of who is missing.

:pray: Thanks everybody for your kind cooperation and help.
"""


def _get_previous_version(vtag: str) -> int:
    version_parts = vtag.strip("v").split(".")
    version_parts[1] = f"{int(version_parts[1])-1}"

    return "v" + ".".join(version_parts)


def _get_names_to_check() -> str:
    return "\n".join([f"- [ ] {name}" for name in INITIALS])


def main():
    parser = argparse.ArgumentParser(
        description="Process a version number in the format X.X.X"
    )
    parser.add_argument(
        "version", type=validate_version, help="The version number in the format X.X.X"
    )
    parser.add_argument(
        "deadline_day",
        type=validate_date,
        help="The date is in the format dd.mm",
    )
    parser.add_argument(
        "deadline_time",
        type=validate_time,
        help="The time is in the format HH:MM",
    )

    args = parser.parse_args()
    tag = f"{args.version}"

    vtag = f"v{tag}"

    print("\nTotal [STEPS] 2\n")

    print(f"Will generate form tag: {vtag}")

    new_draft_content = _TEMPLATE.format(
        version_tag=_get_previous_version(vtag), names_to_check=_get_names_to_check()
    )
    for product_folder in list_folders_in_path(CURRENT_DIR / ".." / "release-notes"):
        draft_file = product_folder / f"{vtag}.md"
        if draft_file.exists():
            msg = f"{draft_file} already exists, make sure you are creating the draft for the correct release"
            raise ValueError(msg)
        draft_file.write_text(new_draft_content)

    print(
        "\n[STEP] 1/2 post this message on mattermost, please edit the DEADLINE accordingly\n"
    )
    print(
        _MATTERMOST_TEMPLATE.format(
            version_tag=vtag,
            deadline_day=args.deadline_day,
            deadline_time=args.deadline_time,
        )
    )

    print("\n[STEP] 2/2 commit and push changes generated in this repo!!!!\n")


if __name__ == "__main__":
    main()
