import requests

def get_all_issues(owner, repo, state, labels, since):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    params = {
        "state": state,
        "labels": labels,
        "since": since,
        "per_page": 100  # GitHub allows up to 100 issues per page
    }
    headers = {"Accept": "application/vnd.github.v3+json"}
    issues = []
    page = 1

    while True:
        response = requests.get(url, params={**params, "page": page}, headers=headers)
        response_data = response.json()
        if not response_data:
            break
        issues.extend(response_data)
        page += 1

    return issues

def print_issues(issues):
    for issue in issues:
        title = issue['title']
        issue_number = issue['number']
        issue_url = issue['html_url']
        closed_at = issue['closed_at']
        print(f"- {title} [#{issue_number}]({issue_url}) closed {closed_at}")

if __name__ == "__main__":
    owner = "ITISFoundation"
    repo = "osparc-simcore"
    state = "closed"
    labels = "t:maintenance"
    since = "2024-07-01T00:00:00Z"
    
    issues = get_all_issues(owner, repo, state, labels, since)
    print_issues(issues)
