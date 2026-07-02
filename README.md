# osparc-issues

[![Join the chat at https://gitter.im/osparc-support/community](https://badges.gitter.im/osparc-support/community.svg)](https://gitter.im/osparc-support/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This is an [issue-only repo](https://help.github.com/en/articles/creating-an-issues-only-repository) for the **osparc project**

- 🚩[milestones](https://github.com/ITISFoundation/osparc-issues/milestones)
- 🏷️ [issues](https://github.com/ITISFoundation/osparc-issues/issues)
  - Create a [new issue](https://github.com/ITISFoundation/osparc-issues/issues/new/choose)  ?
- 📅 [reviews](reviews) - agenda & report on every sprint review
- 🏆 [SM_counts](SM_counts) - Scrum Masters rankings (by counts)

## To manage milestones in multiple repositories

- firstly you need to create a github token
  - in Github settings -> Personal access tokens -> Fine-grained tokens -> *Generate new token*
    - Change resource owner -> ITISFoundation
    - Choose Repository access -> All repositories
    - Choose Permissions -> Repository permissions -> Issues (Read and Write)
  - Now somebody with organization admin rights must approve your token
- use the code in scripts/milestones.py
- do the following

```bash
# to show the help#
make
# to install the requirements
make devenv
source .venv/bin/activate
# to manage milestones
# NOTE: you need a token in github to run these recipes
# In order to use these scripts one needs to:
# - get a Personal Access Token on github: https://github.com/settings/tokens?type=beta
#   - Resource owner must be ITISFoundation
#   - Repository access must be: All repositories
#   - Permissions on repositories: Issues ReadWrite

# to create a new milestone (due date defaults to 20 days from now)
make new-milestone token=GITHUB_TOKEN title="dummy-name"

# to modify a milestone's title, due date and/or state
make modify-milestone token=GITHUB_TOKEN title="dummy-name" ntitle="new-name" ndate="2030-03-12" nstate=closed

# to close a milestone (shortcut for modify-milestone ... nstate=closed)
make close-milestone token=GITHUB_TOKEN title="dummy-name"

# to list milestones across repos (optional title=<filter>, state=open|closed|all, default: open)
make list-milestones token=GITHUB_TOKEN
make list-milestones token=GITHUB_TOKEN title="dummy" state=all
```

The code to create/modify/list milestones uses a hard-coded list of repositories, don't be shy update it if it's missing information.
Also, as this is open source, just feel free to improve the code...
Note: deleting milestones is currently not supported by these recipes; closing a milestone (`nstate=closed`) hides it from the default open view without losing its history or links from issues.
