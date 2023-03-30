import datetime

import arrow
import requests
import typer

app = typer.Typer()

_DEFAULT_REPOS = [
    "osparc-simcore",
    "osparc-ops-environments",
    "dockerfiles",
    "cookiecutter-osparc-service",
    "osparc-services",
    "osparc-issues",
    "osparc-python-runner",
    "osparc-deployment-agent",
]


def _list_organization_repos(token: str, org: str) -> list[str]:
    url = f"https://api.github.com/orgs/{org}/repos"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise RuntimeError(f"Could not list {org} repositories, {response.json()}")

    list_of_repos = response.json()
    return [repo["name"] for repo in list_of_repos]


@app.command()
def create_milestones(
    token: str = typer.Option(...),
    username: str = typer.Option(...),
    repos: list[str] = typer.Option(_DEFAULT_REPOS),
    title: str = typer.Option(...),
    description: str = "",
    due_on: datetime.datetime = datetime.datetime.now() + datetime.timedelta(days=20),
):
    """
    Create milestones in multiple GitHub repositories.
    Example:
    python milestones.py create-milestone --repos osparc-simcore --repos osparc-issues --token TOKEN --username ITISFoundation --title "My awesome sprint name" --description "this sprint is great"
    """
    for repo in repos:
        url = f"https://api.github.com/repos/{username}/{repo}/milestones"
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
        }
        data = {
            "title": title,
            "description": description,
            "due_on": f"{arrow.get(due_on)}",
        }
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 201:
            typer.echo(f"Milestone created successfully in {repo}")
        else:
            typer.echo(f"Failed to create milestone in {repo}: {response.json()}")


@app.command()
def delete_milestones(
    token: str = typer.Option(...),
    username: str = typer.Option(...),
    repos: list[str] = typer.Option(_DEFAULT_REPOS),
    title: str = typer.Option(...),
):
    """
    Delete milestones with the given title in multiple GitHub repositories.
    """
    for repo in repos:
        url = f"https://api.github.com/repos/{username}/{repo}/milestones"
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
        }
        params = {"state": "open"}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            milestones = response.json()
            for milestone in milestones:
                if milestone["title"] == title:
                    milestone_number = milestone["number"]
                    delete_url = f"{url}/{milestone_number}"
                    delete_response = requests.delete(delete_url, headers=headers)
                    if delete_response.status_code == 204:
                        typer.echo(
                            f"Milestone '{title}' deleted successfully in {repo}"
                        )
                    else:
                        typer.echo(f"Failed to delete milestone '{title}' in {repo}")
        else:
            typer.echo(f"Failed to get milestones in {repo}")


if __name__ == "__main__":
    app()
