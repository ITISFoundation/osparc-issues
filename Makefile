.DEFAULT_GOAL := help
SHELL := /bin/bash

.PHONY: help

help: ## help on rule's targets
	@awk --posix 'BEGIN {FS = ":.*?## "} /^[[:alpha:][:space:]_-]+:.*?## / {printf "%-24s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

#
# Environment
#

.venv:
	@python3 --version
	uv venv $@
	## upgrading tools to latest version in $(shell python3 --version)
	@uv pip list --verbose

.PHONY: devenv
devenv: .venv ## setup dev environment
	# install scripts tools
	uv pip --quiet install --requirement \
		scripts/requirements.txt
	# Installing pre-commit hooks in current .git repo
	@$</bin/pre-commit install
	@echo "To activate the venv, execute 'source .venv/bin/activate'"


.PHONY: .check-clean clean

_git_clean_args := -dx --force --exclude=.vscode --exclude=TODO.md --exclude=.venv --exclude=.python-version --exclude="*keep*"

.check-clean:
	@git clean -n $(_git_clean_args)
	@echo -n "Are you sure? [y/N] " && read ans && [ $${ans:-N} = y ]
	@echo -n "$(shell whoami), are you REALLY sure? [y/N] " && read ans && [ $${ans:-N} = y ]


clean: .check-clean ## cleans all unversioned files in project and temp files create by this makefile
	# Cleaning unversioned
	@git clean $(_git_clean_args)


clean-venv: devenv ## Purges .venv into original configuration
	# Cleaning your venv
	uv pip sync --quiet $(CURDIR)/requirements/devenv.txt
	@uv pip list

clean-hooks: ## Uninstalls git pre-commit hooks
	@-pre-commit uninstall 2> /dev/null || rm .git/hooks/pre-commit



#
# Github API
#

.PHONY: .check-github-token
.check-github-token:
	$(if $(token),,$(eval token := $(GITHUB_API_TOKEN)))
	$(if $(token),,$(eval token := $(shell read -p "Enter your GitHub API token: " t && echo $$t)))
	$(if $(token),,$(error No GitHub API token provided))
	$(eval export token=$(token))


.PHONY: new-token
new-token: ## open page to create a new API token
	open https://github.com/settings/personal-access-tokens

.PHONY: new-milestone
new-milestone: .venv .check-github-token ## creates a new milestone in the Github repositories (use title=<milestone title>)
	$(call check_defined, token)
	$(call check_defined, title)
	$</bin/python scripts/milestones.py --token $(token) milestones create \
		--title "$(title)"

.PHONY: modify-milestone
modify-milestone: .venv .check-github-token ## modify a milestone title and/or due date and/or state (use ntitle=newtitle and ndate=2025-07-07 and nstate=open or nstate=closed)
	$(call check_defined, token)
	$(call check_defined, title)
	$</bin/python scripts/milestones.py --token $(token) milestones modify \
		--title "$(title)" \
		$(if $(ntitle),--new-title "$(ntitle)",) \
		$(if $(ndate),--new-due-on "$(ndate)",) \
		$(if $(nstate),--new-state "$(nstate)",)

.PHONY: close-milestone
close-milestone: .venv .check-github-token ## closes an existing milestone (use title=<title>)
	$(call check_defined, token)
	$(call check_defined, title)
	$</bin/python scripts/milestones.py --token $(token) milestones modify \
		--title "$(title)" \
		--new-state closed

.PHONY: list-milestones
list-milestones: .venv .check-github-token ## lists milestones across repos (optional title=<filter> state=open|closed|all)
	$(call check_defined, token)
	$</bin/python scripts/milestones.py --token $(token) milestones list \
		$(if $(title),--title-filter "$(title)",) \
		$(if $(state),--state $(state),)


.PHONY: list-milestone-issues
list-milestone-issues: .venv .check-github-token ## lists open issues on a milestone across repos (use title=<milestone title>, optional assignee=<github user>)
	$(call check_defined, token)
	$(call check_defined, title)
	$</bin/python scripts/milestones.py --token $(token) issues list \
		--milestone "$(title)" \
		$(if $(assignee),--assignee "$(assignee)",)


.PHONY: move-milestone-issues
move-milestone-issues: .venv .check-github-token ## moves open issues from one milestone to another after showing the plan and asking to type MOVE (use title=<source> newtitle=<target>, optional assignee=<github user> dryrun=1 to only preview)
	$(call check_defined, token)
	$(call check_defined, title)
	$(call check_defined, newtitle)
	$</bin/python scripts/milestones.py --token $(token) issues move \
		--from-milestone "$(title)" \
		--to-milestone "$(newtitle)" \
		$(if $(assignee),--assignee "$(assignee)",) \
		$(if $(dryrun),--dry-run,)


# Check that given variables are set and all have non-empty values,
# exit with an error otherwise.
#
# Params:
#   1. Variable name(s) to test.
#   2. (optional) Error message to print.
check_defined = \
    $(strip $(foreach 1,$1, \
        $(call __check_defined,$1,$(strip $(value 2)))))
__check_defined = \
    $(if $(value $1),, \
      $(error Undefined $1$(if $2, ($2))))
