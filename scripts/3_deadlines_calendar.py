import argparse
from datetime import datetime
from typing import Final

TEMPLATE: Final[
    str
] = """## Deadlines & upcoming schedule
{sorted_events}
"""


def validate_date(date_str: str) -> datetime:
    try:
        return datetime.strptime(date_str, "%d.%m")
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Invalid date format: '{date_str}'. Expected format is dd.mm."
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Assemble deadlines calendar")
    for date in [
        "prs_merge",
        "staging_release",
        "review_meeting",
        "start_app_team",
        "end_app_team",
        "prod_release",
    ]:
        parser.add_argument(
            date, type=validate_date, help="The date is in the format dd.mm"
        )
    args = parser.parse_args()
    print(f"\nDeadlines: {args}")
    events = [
        (
            args.prs_merge,
            "`{}`: @all have all your PRs intended to be tested merged by the end of the day",
        ),
        (args.staging_release, "`{}`: STAGING release"),
        (args.review_meeting, "`{}`: REVIEW MEETING"),
        (
            args.review_meeting,
            "`{}`: by the end of the day created draft of the release notes",
        ),
        (
            args.start_app_team,
            "`{}` -> `{}`: App Team has exclusive access to the AWS Staging environment",
        ),
        (args.prod_release, "`{}`: PROD release"),
    ]
    events.sort()
    sorted_events = "\n".join(
        event[1].format(event[0].strftime("%d.%m"), args.end_app_team.strftime("%d.%m"))
        for event in events
    )
    mattermost_message = TEMPLATE.format(sorted_events=sorted_events)
    print(f"\n{mattermost_message}\n")


if __name__ == "__main__":
    main()
