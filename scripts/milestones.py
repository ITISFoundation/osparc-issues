"""
In order to use these scripts one needs to get a

"Personal Access Token" on github:
    https://github.com/settings/personal-access-tokens (or `make new-token`)

Then:
  - Resource owner MUST be `ITISFoundation`
  - Repository access MUST be: `All repositories`
  - Permissions on repositories MUST be: `Issues` with `Access:Read and write`
"""

import datetime
from dataclasses import dataclass, field
from enum import Enum
from http import HTTPStatus
from typing import Annotated, Final

import arrow
import requests
import typer

app = typer.Typer()
milestone_app = typer.Typer(help="Manage milestones across GitHub repositories")
issues_app = typer.Typer(help="Manage issues across GitHub repositories")
app.add_typer(milestone_app, name="milestones")
app.add_typer(issues_app, name="issues")

_DEFAULT_REPOS = [
    "cookiecutter-osparc-service",
    "dockerfiles",
    "hornet-manifest-spec",
    "osparc-issues",
    "osparc-ops-environments",
    "osparc-python-runner",
    "osparc-services",
    "osparc-simcore-clients",
    "osparc-simcore",
    "private-issues",
]

_REQUEST_TIMEOUT: Final[int] = 10  # seconds
_FAILED_EXIT_CODE: Final[int] = 127


#
# common context (set once by the root callback from --token/--username/--repos)
#


@dataclass
class _Context:
    token: str | None = None
    username: str = "ITISFoundation"
    repos: list[str] = field(default_factory=lambda: list(_DEFAULT_REPOS))


_context: _Context | None = None


def _ctx() -> _Context:
    """Return the parsed common context, ensuring --token was provided.

    --token is only checked here (not required in the callback) so that
    '--help' still works on the command groups themselves.
    """
    ctx = _context if _context is not None else _Context()
    if not ctx.token:
        _echo_error(
            "Missing --token: pass the GitHub personal access token"
            " before the subcommand, e.g."
            " 'milestones.py --token TOKEN milestones list'."
            " See also 'make new-token'."
        )
        raise typer.Exit(_FAILED_EXIT_CODE)
    return ctx


@app.callback()
def main(
    token: Annotated[
        str | None,
        typer.Option(help="GitHub personal access token"),
    ] = None,
    username: Annotated[
        str,
        typer.Option(help="GitHub organization, e.g. ITISFoundation"),
    ] = "ITISFoundation",
    repos: Annotated[
        list[str], typer.Option(help="Repositories to operate on")
    ] = _DEFAULT_REPOS,
):
    """GitHub milestone/issue maintenance helpers for the ITISFoundation org.

    Use 'milestones' subcommands (create/modify/list) or 'issues' subcommands
    (list/move). The common options above must come BEFORE the subcommand.
    """
    global _context
    _context = _Context(token=token, username=username, repos=list(repos))


#
# colored output helpers
#


def _echo_error(msg: str) -> None:
    typer.echo(typer.style(msg, fg=typer.colors.RED), err=True)


def _echo_ok(msg: str) -> None:
    typer.echo(typer.style(msg, fg=typer.colors.GREEN))


def _echo_repo_header(repo: str, count: int, noun: str) -> None:
    color = typer.colors.YELLOW if count else typer.colors.GREEN
    typer.echo(
        typer.style(repo, bold=True)
        + " "
        + typer.style(f"({count} {noun}):", fg=color, bold=True)
    )


def _echo_summary(msg: str) -> None:
    typer.echo(typer.style(msg, bold=True))


def _print_issue(issue: dict, *, show_url: bool = True) -> None:
    labels = ", ".join(label["name"] for label in issue["labels"])
    assignees = ", ".join(a["login"] for a in issue["assignees"])
    line = (
        "  "
        + typer.style(f"#{issue['number']}", fg=typer.colors.MAGENTA, bold=True)
        + f" {issue['title']}"
        + typer.style(f"  [labels: {labels or '-'}]", fg=typer.colors.GREEN)
        + typer.style(f"  [assignees: {assignees or '-'}]", fg=typer.colors.CYAN)
    )
    if show_url:
        line += typer.style(f"  {issue['html_url']}", dim=True)
    typer.echo(line)


def _list_organization_repos(token: str, org: str) -> list[str]:
    url = f"https://api.github.com/orgs/{org}/repos"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    response = requests.get(url, headers=headers, timeout=_REQUEST_TIMEOUT)
    if response.status_code != HTTPStatus.OK:
        raise RuntimeError(
            f"Could not list {org} repositories, {response.reason} with {response.json()}"
        )

    list_of_repos = response.json()
    return [repo["name"] for repo in list_of_repos]


class StateEnum(str, Enum):
    open = "open"
    closed = "closed"


class ListStateEnum(str, Enum):
    open = "open"
    closed = "closed"
    all = "all"


def _default_due_on() -> datetime.datetime:
    return arrow.utcnow().shift(days=20).datetime


@milestone_app.command("create")
def create(
    title: Annotated[str, typer.Option(help="Milestone title")],
    due_on: Annotated[
        datetime.datetime,
        typer.Option(default_factory=_default_due_on, help="Due date"),
    ],
    description: Annotated[str, typer.Option(help="Milestone description")] = "",
):
    """
    Create milestone in multiple GitHub repositories.
    Example:
    python milestones.py --token TOKEN milestones create --title "My awesome sprint name" --description "this sprint is great"
    """
    ctx = _ctx()
    for repo in ctx.repos:
        url = f"https://api.github.com/repos/{ctx.username}/{repo}/milestones"
        headers = _github_headers(ctx.token)
        data = {
            "title": title,
            "description": description,
            "due_on": f"{arrow.get(due_on)}",
        }
        response = requests.post(
            url, headers=headers, json=data, timeout=_REQUEST_TIMEOUT
        )

        if response.status_code == HTTPStatus.CREATED:
            _echo_ok(f"Milestone created successfully in {repo}")
        else:
            _echo_error(
                f"Failed to create milestone in {repo}: {response.reason} with {response.json()}"
            )


@milestone_app.command("modify")
def modify(
    title: Annotated[str, typer.Option(help="Existing milestone title")],
    new_title: Annotated[str | None, typer.Option(help="New title")] = None,
    new_description: Annotated[str | None, typer.Option(help="New description")] = None,
    new_due_on: Annotated[
        datetime.datetime | None, typer.Option(help="New due date")
    ] = None,
    new_state: Annotated[StateEnum | None, typer.Option(help="New state")] = None,
):
    """
    Modify milestone in multiple GitHub repositories.
    Example:
    python milestones.py --token TOKEN milestones modify --title "My awesome sprint name" --new-description "this sprint is great"
    """
    ctx = _ctx()
    data = {}
    if new_title:
        data["title"] = new_title
    if new_description:
        data["description"] = new_description
    if new_due_on:
        data["due_on"] = f"{arrow.get(new_due_on)}"
    if new_state:
        data["state"] = new_state.value

    if not data:
        _echo_error(f"Nothing to modify in {title}, wrong call?")
        raise typer.Exit(_FAILED_EXIT_CODE)

    milestone_found = False
    for repo in ctx.repos:
        url = f"https://api.github.com/repos/{ctx.username}/{repo}/milestones"
        headers = _github_headers(ctx.token)
        params = {"state": "open"}
        response = requests.get(
            url, headers=headers, params=params, timeout=_REQUEST_TIMEOUT
        )

        if response.status_code == HTTPStatus.OK:
            milestones = response.json()
            for milestone in milestones:
                if milestone["title"] == title:
                    milestone_found = True
                    milestone_number = milestone["number"]
                    modify_url = f"{url}/{milestone_number}"
                    modify_response = requests.patch(
                        modify_url, headers=headers, json=data, timeout=_REQUEST_TIMEOUT
                    )
                    if modify_response.status_code == HTTPStatus.OK:
                        _echo_ok(f"Milestone '{title}' modified successfully in {repo}")
                    else:
                        _echo_error(
                            f"Failed to modify milestone '{title}' in {repo}: {modify_response.reason}"
                        )
        else:
            _echo_error(f"Failed to get milestones in {repo}: {response.reason}")
            raise typer.Exit(_FAILED_EXIT_CODE)
    if not milestone_found:
        _echo_error(f"Failed to find {title} in any of {ctx.repos}")
        raise typer.Exit(_FAILED_EXIT_CODE)


@milestone_app.command("list")
def list_milestones(
    title_filter: Annotated[
        str | None,
        typer.Option(help="Only show milestones whose title contains this substring"),
    ] = None,
    state: Annotated[
        ListStateEnum, typer.Option(help="Milestone state")
    ] = ListStateEnum.open,
):
    """
    List milestones across multiple GitHub repositories.
    Example:
    python milestones.py --token TOKEN milestones list --state open
    """
    ctx = _ctx()
    headers = _github_headers(ctx.token)
    found_any = False
    for repo in ctx.repos:
        url = f"https://api.github.com/repos/{ctx.username}/{repo}/milestones"
        params = {"state": state.value}
        response = requests.get(
            url, headers=headers, params=params, timeout=_REQUEST_TIMEOUT
        )
        if response.status_code != HTTPStatus.OK:
            _echo_error(f"Failed to get milestones in {repo}: {response.reason}")
            continue

        milestones = [
            milestone
            for milestone in response.json()
            if not title_filter or title_filter.lower() in milestone["title"].lower()
        ]
        if not milestones:
            continue
        found_any = True
        typer.echo()  # separate repositories
        typer.echo(typer.style(repo, bold=True, underline=True))
        for milestone in milestones:
            state_color = (
                typer.colors.GREEN if milestone["state"] == "open" else typer.colors.RED
            )
            state_str = typer.style(
                f"{milestone['state']:<6}", fg=state_color, bold=True
            )
            due_str = typer.style(milestone.get("due_on") or "-", dim=True)
            typer.echo(
                f"  #{milestone['number']:<4} [{state_str}] "
                f"{milestone['title']:30} due:{due_str}"
            )

    if not found_any:
        _echo_summary("No milestones found matching criteria")


def _github_headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
    }


def _find_milestone_number(
    headers: dict, username: str, repo: str, title: str
) -> int | None:
    """Resolve a milestone title to its number in a repo (None if not found).

    Searches with state=all so closed milestones are found too, since the issues
    endpoint rejects milestone titles that are not open.
    """
    ms_url = f"https://api.github.com/repos/{username}/{repo}/milestones"
    ms_response = requests.get(
        ms_url,
        headers=headers,
        params={"state": "all", "per_page": 100},
        timeout=_REQUEST_TIMEOUT,
    )
    if ms_response.status_code != HTTPStatus.OK:
        _echo_error(f"Failed to get milestones in {repo}: {ms_response.reason}")
        return None
    return next(
        (
            ms["number"]
            for ms in ms_response.json()
            if ms["title"].lower() == title.lower()
        ),
        None,
    )


def _get_open_issues_on_milestone(
    headers: dict, username: str, repo: str, milestone_number: int
) -> list[dict]:
    """Return open issues (no pull requests) on the given milestone number."""
    url = f"https://api.github.com/repos/{username}/{repo}/issues"
    params = {
        "state": "open",
        "milestone": str(milestone_number),
        "per_page": 100,
    }
    response = requests.get(
        url, headers=headers, params=params, timeout=_REQUEST_TIMEOUT
    )
    if response.status_code != HTTPStatus.OK:
        _echo_error(
            f"Failed to get issues in {repo}: {response.reason} with {response.json()}"
        )
        return []
    return [issue for issue in response.json() if "pull_request" not in issue]


def _filter_by_assignee(issues: list[dict], assignee: str | None) -> list[dict]:
    if not assignee:
        return issues
    return [
        issue
        for issue in issues
        if any(a["login"].lower() == assignee.lower() for a in issue["assignees"])
    ]


@issues_app.command("list")
def list_issues(
    milestone: Annotated[str, typer.Option(help="Milestone title, e.g. KonradZuse")],
    assignee: Annotated[
        str | None,
        typer.Option(help="Only issues assigned to this GitHub user (default: any)"),
    ] = None,
):
    """
    List open (not closed) issues assigned to a milestone across multiple GitHub repositories.
    Optionally filter by assignee.
    Example:
    python milestones.py --token TOKEN issues list --milestone KonradZuse --assignee sanderegg
    """
    ctx = _ctx()
    headers = _github_headers(ctx.token)
    total_open = 0
    for repo in ctx.repos:
        milestone_number = _find_milestone_number(
            headers, ctx.username, repo, milestone
        )
        if milestone_number is None:
            continue  # milestone does not exist in this repo

        issues = _filter_by_assignee(
            _get_open_issues_on_milestone(
                headers, ctx.username, repo, milestone_number
            ),
            assignee,
        )
        if not issues:
            continue
        _echo_repo_header(repo, len(issues), "open")
        for issue in issues:
            _print_issue(issue)
        total_open += len(issues)

    filtered = f" assigned to {assignee}" if assignee else ""
    total_color = typer.colors.YELLOW if total_open else typer.colors.GREEN
    _echo_summary(
        f"Total open issues{filtered} on milestone"
        f" '{milestone}': {typer.style(str(total_open), fg=total_color, bold=True)}"
    )


@issues_app.command("move")
def move_issues(
    from_milestone: Annotated[str, typer.Option(help="Source milestone title")],
    to_milestone: Annotated[str, typer.Option(help="Target milestone title")],
    assignee: Annotated[
        str | None,
        typer.Option(help="Only issues assigned to this GitHub user (default: any)"),
    ] = None,
    dry_run: Annotated[
        bool,
        typer.Option(
            help="Only show what would be moved, without asking or changing anything"
        ),
    ] = False,
    yes: Annotated[
        bool,
        typer.Option(
            help="Skip the interactive confirmation prompt (becomes --yes/--no-yes)"
        ),
    ] = False,
):
    """
    Move open issues from one milestone to another across multiple GitHub repositories,
    optionally limited to issues assigned to a specific user.
    Always shows the full plan first and requires typing MOVE (or --yes) to proceed.
    Example:
    python milestones.py --token TOKEN issues move --from-milestone KonradZuse --to-milestone AdaLovelace --assignee sanderegg
    """
    ctx = _ctx()
    headers = _github_headers(ctx.token)
    filtered = f" assigned to {assignee}" if assignee else ""

    # 1) build the plan first: verify milestones and collect matching issues per repo
    plan: list[tuple[str, int, list[dict]]] = []  # (repo, target_number, issues)
    missing_targets: list[str] = []
    for repo in ctx.repos:
        source_number = _find_milestone_number(
            headers, ctx.username, repo, from_milestone
        )
        if source_number is None:
            continue  # source milestone does not exist in this repo
        target_number = _find_milestone_number(
            headers, ctx.username, repo, to_milestone
        )
        if target_number is None:
            missing_targets.append(repo)
            continue

        issues = _filter_by_assignee(
            _get_open_issues_on_milestone(headers, ctx.username, repo, source_number),
            assignee,
        )
        if issues:
            plan.append((repo, target_number, issues))

    if missing_targets:
        _echo_error(
            f"ERROR: target milestone '{to_milestone}' does not exist in"
            f" {', '.join(missing_targets)} (where '{from_milestone}' exists)."
            " Create it first (e.g. 'make new-milestone') — aborting."
        )
        raise typer.Exit(_FAILED_EXIT_CODE)

    # 2) always print the dry-run plan
    total_planned = 0
    for repo, _target_number, issues in plan:
        _echo_repo_header(repo, len(issues), "to move")
        for issue in issues:
            _print_issue(issue, show_url=False)
        total_planned += len(issues)
    planned_color = typer.colors.YELLOW if total_planned else typer.colors.GREEN
    _echo_summary(
        f"Would move{filtered}:"
        f" {typer.style(str(total_planned), fg=planned_color, bold=True)} issue(s) from"
        f" '{typer.style(from_milestone, bold=True)}' to"
        f" '{typer.style(to_milestone, bold=True)}'"
    )

    if dry_run:
        raise typer.Exit(0)
    if total_planned == 0:
        typer.echo("Nothing to move")
        raise typer.Exit(0)

    # 3) require an explicit confirmation word before making any change
    if not yes:
        answer = typer.prompt(
            typer.style(
                f"Type MOVE to move {total_planned} issue(s) to"
                f" '{to_milestone}', anything else to abort",
                fg=typer.colors.YELLOW,
            )
        )
        if answer.strip().upper() != "MOVE":
            typer.echo(typer.style("Aborted, no changes made", fg=typer.colors.YELLOW))
            raise typer.Exit(0)

    # 4) perform the moves
    total_moved = 0
    for repo, target_number, issues in plan:
        for issue in issues:
            assignees = ", ".join(a["login"] for a in issue["assignees"])
            issue_url = f"https://api.github.com/repos/{ctx.username}/{repo}/issues/{issue['number']}"
            patch_response = requests.patch(
                issue_url,
                headers=headers,
                json={"milestone": target_number},
                timeout=_REQUEST_TIMEOUT,
            )
            if patch_response.status_code == HTTPStatus.OK:
                assignees_part = typer.style(
                    f"  [assignees: {assignees or '-'}]", fg=typer.colors.CYAN
                )
                _echo_ok(
                    f"  moved {repo}"
                    f"#{typer.style(str(issue['number']), fg=typer.colors.MAGENTA, bold=True)}"
                    f" {issue['title']}{assignees_part}"
                )
                total_moved += 1
            else:
                _echo_error(
                    f"  failed to move {repo}#{issue['number']}:"
                    f" {patch_response.reason} with {patch_response.json()}"
                )

    moved_color = (
        typer.colors.GREEN if total_moved == total_planned else typer.colors.RED
    )
    _echo_summary(
        f"Moved{filtered}:"
        f" {typer.style(f'{total_moved}/{total_planned}', fg=moved_color, bold=True)}"
        f" issue(s) from '{from_milestone}' to '{to_milestone}'"
    )


if __name__ == "__main__":
    app()
