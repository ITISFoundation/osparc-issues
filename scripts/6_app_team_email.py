import argparse
from typing import Final

from utils import validate_date, validate_version

_TEMPLATE: Final[
    str
] = """
Dear App Team,

please find below some more details about testing of the staging deployments and release notes improvements.

Starting evniroment is available from `{start_app_team}` to `{end_app_team}`. Please use the following these deployments (not for production work):
- osparc https://osparc-staging.io/
- s4l lite https://staging.s4l-lite.io/
- s4l https://sim4life-staging.cloud/

This is the draft of the release notes: https://github.com/ITISFoundation/osparc-issues/blob/master/release-notes/s4l/{vtag}.md
We have added some highlights for you.

We would like your input on the following:
- Rewrite of the draft release notes, in a more user-friendly fashion
- Test the deployments, including the highlights it they make sense to you
- Let us know if something is not working/showing as expected
- Please let us know if you don't have accounts yet on some of those deployments


Regards,
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Assemble deadelines calendar")
    for date in [
        "start_app_team",
        "end_app_team",
    ]:
        parser.add_argument(
            date,
            type=validate_date,
            help="The version number in the format dd.mm",
        )
    parser.add_argument(
        "version", type=validate_version, help="The version number in the format X.X.X"
    )

    args = parser.parse_args()
    print(f"\nArguments: {args}")

    email_content = _TEMPLATE.format(
        start_app_team=args.start_app_team,
        end_app_team=args.end_app_team,
        vtag=f"v{args.version}",
    )

    print(email_content)
    print("\n!!Please review and feel free to edit above text!!\n")


if __name__ == "__main__":
    main()
