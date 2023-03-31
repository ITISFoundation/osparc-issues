.DEFAULT_GOAL := help
SHELL := /bin/bash

.PHONY: help

help: ## help on rule's targets
	@awk --posix 'BEGIN {FS = ":.*?## "} /^[[:alpha:][:space:]_-]+:.*?## / {printf "%-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.venv:
	@python3 --version
	python3 -m venv $@
	## upgrading tools to latest version in $(shell python3 --version)
	$@/bin/pip3 --quiet install --upgrade \
		pip~=23.0 \
		wheel \
		setuptools
	@$@/bin/pip3 list --verbose

.PHONY: devenv
devenv: .venv ## setup dev environment
	# upgrades install tools
	$</bin/pip3 --quiet install -U \
		pip \
		setuptools \
		wheel
	# install scripts tools
	$</bin/pip3 --quiet install --requirement \
		scripts/requirements.txt
	# Installing pre-commit hooks in current .git repo
	@$</bin/pre-commit install
	@echo "To activate the venv, execute 'source .venv/bin/activate'"

.PHONY: new-token
new-token:
	open https://github.com/settings/tokens?type=beta

.PHONY: new-milestone
new-milestone: .venv ## creates a new milestone in the Github repositories
	$(call check_defined, token)
	$(call check_defined, title)
	$</bin/python scripts/milestones.py create \
		--token $(token) \
		--username ITISFoundation \
		--title "$(title)"

modify-milestone: .venv ## modifiy a milestone title and/or due date and/or state (use ntitle= and ndate= and nstate=open or nstate=closed)
	$(call check_defined, token)
	$(call check_defined, title)
	$</bin/python scripts/milestones.py modify \
		--token $(token) \
		--username ITISFoundation \
		--title "$(title)" \
		$(if $(findstring ntitle, $(MAKEFLAGS)),--new-title "$(ntitle)",) \
		$(if $(findstring ndate, $(MAKEFLAGS)),--new-due-on "$(ndate)",) \
		$(if $(findstring nstate, $(MAKEFLAGS)),--new-state "$(nstate)",) \

delete-milestone: .venv ## delete a milestone, use with care!!
	@echo -n "Are you sure? [y/N] " && read ans && [ $${ans:-N} = y ]
	$(call check_defined, token)
	$(call check_defined, title)
	$</bin/python scripts/milestones.py delete \
		--token $(token) \
		--username ITISFoundation \
		--title "$(title)"

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
