import argparse
from typing import Final

from utils import validate_date

TEMPLATE: Final[
    str
] = """

## Deadlines & upcoming schedule
`{prs_merge}`: @all have all your PRs intended to be tested merged by the end of the day
`{staging_release}`: STAGING release
`{review_meeting}`: REVIEW MEETING
`{review_meeting}`: by the end of the day created draft of the release notes
`{start_app_team}`: -> {end_app_team}: App Team has exclusive access to the AWS Staging environment
`{prod_release}`: PROD release
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Assemble deadelines calendar")
    for date in [
        "prs_merge",
        "staging_release",
        "review_meeting",
        "start_app_team",
        "end_app_team",
        "prod_release",
    ]:
        parser.add_argument(
            date,
            type=validate_date,
            help="The date is in the format dd.mm",
        )
    args = parser.parse_args()
    print(f"\nDeadlines: {args}")

    mattermost_message = TEMPLATE.format(
        prs_merge=args.prs_merge,
        staging_release=args.staging_release,
        review_meeting=args.review_meeting,
        start_app_team=args.start_app_team,
        end_app_team=args.end_app_team,
        prod_release=args.prod_release,
    )

    print(f"\n{mattermost_message}\n")


if __name__ == "__main__":
    main()
