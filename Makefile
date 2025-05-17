SHELL := /usr/bin/env bash
.SHELLFLAGS := -eu -o pipefail -c

SOURCES = object_mother_pattern
FULL_SOURCES = $(SOURCES) tests
CONFIGURATION_FILE = pyproject.toml 
VERBOSE ?= false
PYTHON_VERSION ?= 3.13
PYTHON_VIRTUAL_ENVIRONMENT ?= .venv


.PHONY: help
help: # It displays this help message
	@printf "\nUsage: make [COMMAND] [OPTIONS]...\n"
	@awk 'BEGIN {FS = ":.*#"; printf "\nCommands:\n  make \033[36m\033[0m\n"} /^[a-zA-Z_-]+:.*?#/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
	@printf "\nOptions (override with VAR=value):\n"
	@printf "  %-40s %s\n" "VERBOSE=$(VERBOSE)"                   "Show command output (true/false)"
	@printf "  %-40s %s\n" "PYTHON_VERSION=$(PYTHON_VERSION)"     "Used python interpreter for creating the virtual environment"
	@printf "  %-40s %s\n" "PYTHON_VIRTUAL_ENVIRONMENT=$(PYTHON_VIRTUAL_ENVIRONMENT)" "Name of the virtual environment folder"
	@printf "\n"



.PHONY: install-dev
install-dev: # It installs development dependencies
	@echo -e "\n⌛ Installing development dependencies...\n"


	@echo -e "\n✅ Development dependencies installed correctly.\n"


install: # An alias for 'make install-dev'


.PHONY: install-prod
install-prod: # It installs production dependencies
	@echo -e "\n⌛ Installing production dependencies...\n"


	@echo -e "\n✅ Production dependencies installed correctly.\n"


.PHONY: format
format: # It automatically formats code
	@echo -e "\n⌛ Formatting project code...\n"

	@$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/ruff check $(FULL_SOURCES) --fix-only --config $(CONFIGURATION_FILE)
	@$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/ruff format $(FULL_SOURCES) --config $(CONFIGURATION_FILE)


.PHONY: lint
lint: # It automatically lints code
	@echo -e "\n⌛ Linting project code...\n"

	@set -e; \
	$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/mypy $(FULL_SOURCES) --txt-report . --config-file $(CONFIGURATION_FILE) || mypy_exit=$$?; \
	$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/ruff check $(FULL_SOURCES) || ruff_exit=$$?; \
	exit $$(( mypy_exit || ruff_exit ))

 
.PHONY: test
test: # It runs all tests
	@echo -e "\n⌛ Running tests...\n"

	@$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/pytest --config-file $(CONFIGURATION_FILE)


.PHONY: coverage
coverage: # It gets the test coverage report
	@echo -e "\n⌛ Getting test coverage report...\n"

	@set -e; \
	$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/coverage erase; \
	$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/coverage run --module pytest --config-file $(CONFIGURATION_FILE) || coverage_exit=$$?; \
	$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/coverage combine; \
	$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/coverage report; \
	exit $$coverage_exit


.PHONY: clean
clean: # It cleans up the project, removing the virtual environment and some files
	@echo -e "\n⌛ Cleaning up the project...\n"


	@echo -e "\n✅ Run 'deactivate' to deactivate the virtual environment.\n"


.PHONY: update-lists
update-lists: # It updates content lists
	@echo -e "\n⌛ Updating content lists...\n"

	@$(PYTHON_VIRTUAL_ENVIRONMENT)/bin/python$(PYTHON_VERSION) update_lists.py

	@echo -e "\n✅ Content lists updated correctly.\n"
