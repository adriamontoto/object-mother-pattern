SHELL := /usr/bin/env bash
.SHELLFLAGS := -eu -o pipefail -c

SOURCES = object_mother_pattern
FULL_SOURCES = $(SOURCES) tests
CONFIGURATION_FILE = pyproject.toml 
VERBOSE ?= false
PYTHON_VERSION ?= 3.13
PYTHON_VIRTUAL_ENVIRONMENT ?= .venv


.PHONY: help
help: # Display this help
	@echo "Usage: make [COMMAND] [OPTIONS]..."
	@awk 'BEGIN {FS = ":.*#"; printf "\nCommands:\n  make \033[36m\033[0m\n"} /^[a-zA-Z_-]+:.*?#/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


.PHONY: install
install: # Install dependencies
	@make install-dev


.PHONY: install-dev
	@$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/pip$(PYTHON_VERSION) install --requirement requirements_dev.txt


.PHONY: install-prod
	@$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/pip$(PYTHON_VERSION) install --requirement requirements.txt


.PHONY: format
	@$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/ruff check $(FULL_SOURCES) --fix-only --config $(CONFIGURATION_FILE)
	@$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/ruff format $(FULL_SOURCES) --config $(CONFIGURATION_FILE)


.PHONY: lint
lint: # Lint python code
	@set -e; \
	$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/mypy $(FULL_SOURCES) --txt-report . --config-file $(CONFIGURATION_FILE) || mypy_exit=$$?; \
	$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/ruff check $(FULL_SOURCES) || ruff_exit=$$?; \
	exit $$(( mypy_exit || ruff_exit ))


.PHONY: test
	@$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/pytest --config-file $(CONFIGURATION_FILE)


.PHONY: coverage
coverage: # Get coverage report
	@set -e; \
	$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/coverage erase; \
	$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/coverage run --module pytest --config-file $(CONFIGURATION_FILE) || coverage_exit=$$?; \
	$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/coverage combine; \
	$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/coverage report; \
	exit $$coverage_exit


.PHONY: clean
clean: # Remove all generated files
	@rm --force --recursive `find . -type f -name '*.py[co]'`
	@rm --force --recursive `find . -name __pycache__`
	@rm --force --recursive `find . -name .ruff_cache`
	@rm --force --recursive `find . -name .mypy_cache`
	@rm --force --recursive `find . -name index.txt`
	@rm --force --recursive `find . -name .pytest_cache`
	@rm --force --recursive .coverage
	@rm --force --recursive .coverage.*
	@rm --force --recursive coverage.xml
	@rm --force --recursive htmlcov

.PHONY: update-lists
	@$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/python$(PYTHON_VERSION) update_lists.py
