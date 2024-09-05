from pathlib import Path
from typing import Final

import requests
from utils import list_folders_in_path, require_tag_from_cli

CURRENT_DIR: Path = Path(__file__).resolve().parent


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
            msg = f"'source target' {soruce_draft_file} does not exist"
            raise ValueError(msg)
        if target_draft_file.exists():
            msg = f"'destination target' {target_draft_file} already exists"
            raise ValueError(msg)

        print(f"copy from {soruce_draft_file} -> {target_draft_file}")
        target_draft_file.write_text(soruce_draft_file.read_text())


def _insert_after_line(text: str, target_line: str, to_insert: str) -> str:
    lines: list[str] = text.split("\n")
    output_lines: list[str] = []

    for line in lines:
        output_lines.append(line)
        if line == target_line:
            for new_line in to_insert.split("\n"):
                output_lines.append(new_line)

    return "\n".join(output_lines)


MANUAL_LINKS: Final[str] = (
    "https://raw.githubusercontent.com/ZurichMedTech/s4l-manual/main/docs/release/releases.md"
)

MANUAL_ENTRY_TEMPLATE = """
<h3 id="v{tag}"><a href="https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v{tag}.md">Version: {tag}</a></h3>

 - Release Date: 22.08.2024
 - [Changelog](https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/v{tag}.md)
"""

INSTRUCTIONS_TEMPLATE: Final[
    str
] = """
Instructions:
- Open https://github.com/ZurichMedTech/s4l-manual/blob/main/docs/release/releases.md#v1.76.1
- click the edit button
- repalce the content with the one form {file}
- create a PR and merge it or ask for MaG to merge it
"""


def get_instructuinf_for_pull_request(tag: str) -> None:
    print("\nEnsure you ran 'make devenv' and 'source .venv/bin/activate'")
    next_tag = _get_next_tag_patch(tag)

    response = requests.get(MANUAL_LINKS, timeout=5)
    manual_content = response.text

    result = _insert_after_line(
        manual_content,
        "## sim4life.io/sim4life.science Platform",
        MANUAL_ENTRY_TEMPLATE.format(tag=next_tag),
    )

    updated_content_file = CURRENT_DIR / f"to_pr_added_tag_{next_tag}.ignore.md"
    updated_content_file.write_text(result)
    print(INSTRUCTIONS_TEMPLATE.format(file=updated_content_file.absolute()))


def main() -> None:
    print("This is a [2 STEP] operation\n")
    print(
        "[NOTE]: make sure the provided version already exists in the product folders!\n"
    )
    tag = require_tag_from_cli()

    # copy existing release notes in this repo
    copy_from_exiting_release(tag)

    print("\n[STEP 1/2] generate a file who's contents need to be pull requested")
    get_instructuinf_for_pull_request(tag)

    print("\n[STEP 2/2] make sure to commit and push changes in this repository!!\n")


if __name__ == "__main__":
    main()
