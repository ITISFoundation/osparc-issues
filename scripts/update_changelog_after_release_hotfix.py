from typing import Final
from pathlib import Path

from utils import list_folders_in_path, require_tag_from_cli

CURRENT_DIR: Path = Path(__file__).resolve().parent
MANUAL_LINKS: Final[str] = (
    "https://raw.githubusercontent.com/ZurichMedTech/s4l-manual/main/docs/release/releases.md"
)

MANUAL_ENTRY_TEMPLATE = """
<h3 id="v{tag}"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v{tag}.md">Version: {tag}</a></h3>
 
 - Release Date: 22.08.2024
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v{tag}.md)
"""


def _get_next_tag_patch(tag: str) -> int:
    version_parts = tag.strip("v").split(".")
    version_parts[2] = f"{int(version_parts[2])+1}"
    return ".".join(version_parts)


def copy_from_exiting_release(tag: str) -> None:
    vtag = f"v{tag}"
    next_tag = _get_next_tag_patch(tag)
    next_vtag = f"v{next_tag}"
    print(f"Will copy release notes from {tag} -> {next_tag}")

    for product_folder in list_folders_in_path(CURRENT_DIR / ".." / "release-notes"):
        soruce_draft_file = product_folder / f"{vtag}.md"
        target_draft_file = product_folder / f"{next_vtag}.md"
        if not soruce_draft_file.exists():
            msg = f"target {soruce_draft_file} dpes mot exist"
            raise ValueError(msg)
        if target_draft_file.exists():
            msg = f"targe {target_draft_file} already exists, please check!"
            raise ValueError(msg)

        print(f"copy from {soruce_draft_file} -> {target_draft_file}")
        target_draft_file.write_text(soruce_draft_file.read_text())


def get_file_to_pr(tag: str) -> None:
    next_tag = _get_next_tag_patch(tag)


def main() -> None:
    tag = require_tag_from_cli()
    # 1. copy existing release notes in this repo
    copy_from_exiting_release(tag)
    # 2. generate a file who's contents need to be pull requested


if __name__ == "__main__":
    main()
