"""
This script generates the .md file for the review agenda (original version by ANE, extended instructions by EI)
Pre-requisite: up-to-date PM2 board
- Go to PM2 Board https://github.com/orgs/ITISFoundation/projects/9/views/23
- Make sure "Topic" is correctly set -> It will be used to group items in the agenda
- Select one row in table
- On your keyboard: press "CTRL+a"
- On your keyboard: press "CTRL+c" (copies table in CSV)
- Create a new csv file in this folder (with the name of the current sprint)
- Paste clipboard
- Create a "mapping_db.ignore.txt": entries in PM2 board have to be present in this file (ask ANE/EI for an example)
- Make sure no other csv file is present in this folder
- Run this script
- Here you go! You have a first version to share with the Team
- Optional: to make the table in the .md file easier to edit, use http://markdowntable.com
"""


import csv
import logging
import re
from pathlib import Path

logger = logging.getLogger("agenda")
logging.basicConfig(level=logging.INFO)


COLUMNS = "Topic Title Presenter Status Duration Start-Time".split()

INITIALS_TO_USERNAMES = {
    "ALL": "Surfict",
    "ANE": "GitHK",
    "BL": "dyollb",
    "CR": "colinRawlings",
    "DK": "mrnicegyu11",
    "EI": "elisabettai",
    "IP": "ignapas",
    "MaG": "mguidon",
    "MB": "bisgaard-itis",
    "MD": "matusdrobuliak66",
    "Nik": "drniiken",
    "OM": "odeimaiz",
    "PC": "pcrespov",
    "SAN": "sanderegg",
    "SB": "sbenkler",
    "SC": "SCA-ZMT",
    "TN": "newton1985",
    "YH": "YuryHrytsuk",
}

USERNAMES_TO_INITIALS = {value: key for key, value in INITIALS_TO_USERNAMES.items()}


def to_md_row(row: list[str]):
    return "|" + "|".join(row) + "|"


def format_status(status):
    if status == "undefined":
        return ""
    elif status != "Paused":
        return f"**{status}**"
    return status


def create_markdown_file(csv_path: Path) -> Path:
    md_path = csv_path.with_suffix(".md")

    with csv_path.open() as csvfile:
        reader = csv.DictReader(csvfile, delimiter="	")

        with md_path.open("wt") as md:
            print(to_md_row(COLUMNS), file=md)
            print(to_md_row(["--"] * len(COLUMNS)), file=md)

            current_topic = None

            issue_numbers = []
            for row in reader:
                # group
                issue = row["Issue"].split("/")[-1]
                issue_numbers.append(issue)
                title = f"[#{issue}] {row['Title']}"
                topic = row["Topic"]
                indented = False
                if topic == current_topic and topic.lower() != "undefined":
                    indented = True
                    title = f"<blockquote>{title}</blockquote>"
                current_topic = topic
                assignees = [
                    f"[{USERNAMES_TO_INITIALS[u]}]"
                    for u in re.findall(r"(\b\w+\b)", row["Assignees"])
                    if u in USERNAMES_TO_INITIALS
                ]
                # write
                col_topic = "" if (indented or topic == "undefined") else topic
                print(
                    to_md_row(
                        [
                            col_topic,  # topic
                            title,  # title
                            ", ".join(assignees),  # presenters
                            format_status(row["Status"]),  # Status
                            "",  # Duration
                            "",  #
                        ]
                    ),
                    file=md,
                )

            print("", file=md)
            for issue in issue_numbers:
                md.writelines(
                    f"[#{issue}]: https://github.com/ITISFoundation/osparc-issues/issues/{issue}\n"
                )

            print("", file=md)
            for acronym in sorted(INITIALS_TO_USERNAMES.keys()):
                username = INITIALS_TO_USERNAMES[acronym]
                print(f"[{acronym}]:https://github.com/{username}", file=md)

    return md_path


def create_md_from_csv():
    for csv_path in Path.cwd().glob("*.csv"):
        logger.info("Processing %s ...", csv_path)
        md_path = create_markdown_file(csv_path)
        logger.info("Created %s", md_path)


def parse_agenda_and_print_links(agenda_md):
    issues = []
    for issue_number in re.findall(r"\[#(\d+)\][^:]", Path(agenda_md).read_text()):
        issues.append(int(issue_number))

    issues = sorted(issues)
    for issue_number in issues:
        # heuristic way to determin the repo
        repo_name = "osparc-issues" if issue_number < 2000 else "osparc-simcore"

        print(
            f"[#{issue_number}]: https://github.com/ITISFoundation/{repo_name}/issues/{issue_number}"
        )


if __name__ == "__main__":
    create_md_from_csv()
    # parse_agenda_and_print_links("../reviews/temp_agenda.md")
