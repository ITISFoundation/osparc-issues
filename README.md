# osparc-issues

[![Join the chat at https://gitter.im/osparc-support/community](https://badges.gitter.im/osparc-support/community.svg)](https://gitter.im/osparc-support/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This is an [issue-only repo](https://help.github.com/en/articles/creating-an-issues-only-repository) for the **osparc project**

-  🚩[milestones](https://github.com/ITISFoundation/osparc-issues/milestones)
- 🏷️ [issues](https://github.com/ITISFoundation/osparc-issues/issues)
  - Create a [new issue](https://github.com/ITISFoundation/osparc-issues/issues/new/choose)  ?
- 📅 [reviews](reviews) - agenda & report on every sprint review
- :trophy: [SM_counts](SM_counts) - Scrum Masters rankings (by counts)


## to create milestones in multiple repositories

- use the code in scripts/milestones.py
- do the following
```bash
# to show the help
make
# to install the requirements
make devenv
source .venv/bin/activate
# to create a milestone
# NOTE: you need a token in github to run these recipes
# In order to use these scripts one needs to:
# - get a Personal Access Token on github: https://github.com/settings/tokens?type=beta
#   - Resource owner must be ITISFoundation
#   - Repository access must be: All repositories
#   - Permissions on repositories: Issues ReadWrite

# to create a new milestone
make new-milestone token=GITHUB_TOKEN title="dummy-name" due_on="2030-03-12"
# to delete the milestone
make delete-milestone token=GITHUB_TOKEN title="dummy-name"
```

The code to create milestone uses a hard-coded list of repositories, don't be shy update it if it's missing information. Also, as this is open source, just feel free to improve the code...
