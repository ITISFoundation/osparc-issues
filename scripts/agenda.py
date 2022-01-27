"""
Go to https://github.com/orgs/ITISFoundation/projects/9/views/1

- select row in table
- CTRL+ a twice (copies table in CSV)
- create a csv file
- paste clipboard
"""


import csv
import logging
from pathlib import Path
from typing import List

logger = logging.getLogger("agenda")
logging.basicConfig(level=logging.INFO)


COLUMNS = "PO Topic Title Presenter Status Duration Start-Time".split()


def to_md_row(row: List[str]):
    return "|" + "|".join(row) + "|"


def to_md(csv_path: Path):
    md_path = csv_path.with_suffix(".md") 

    with csv_path.open() as csvfile:
        reader = csv.DictReader(csvfile)

        with md_path.open("wt") as md:
            print(to_md_row(COLUMNS), file=md)
            print(to_md_row(["--"] * len(COLUMNS)), file=md)
            
            current_topic = None
            for row in reader:
                # group
                title = row["Title"]
                topic = row["Group Topic"]
                indented = False
                if topic == current_topic and topic.lower() != "undefined":
                    indented = True
                    title = f"<blockquote>{title}</blockquote>"
                current_topic = topic
                

                # write
                col_topic ="" if (indented or topic=="undefined") else topic
                print(to_md_row([row["PO Priority"], , title, row["Assignees"], row["Status"], "", "" ]) , file=md)

    return md_path


if __name__ == "__main__":
    for csv_path in Path.cwd().glob("*.csv"):
        logger.info("Processing %s ...", csv_path)
        md_path = to_md(csv_path)
        logger.info("Created %s", md_path)

