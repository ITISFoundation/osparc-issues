


.venv:
	python -m venv .venv


.PHONY: devenv
devenv: .venv
	# upgrades install tools
	.venv/bin/pip install -U \
		pip \
		setuptools \
		wheel
	# installs dev tools
	.venv/bin/pip install \
		black \
		isort
	# install scripts tools
	.venv/bin/pip install --requirement \
	scripts/requirements.txt
	@echo "To activate the venv, execute 'source .venv/bin/activate'"
