SHELL := /usr/bin/env bash
.SHELLFLAGS := -eu -o pipefail -c

SOURCES = object_mother_pattern
FULL_SOURCES = $(SOURCES) tests
CONFIGURATION_FILE = pyproject.toml 
CI ?= false
VERBOSE ?= false
PYTHON_VERSION ?= 3.13
PYTHON_VIRTUAL_ENVIRONMENT ?= .venv


ifeq ($(CI), true)
    PYTHON_BIN = python
else
    PYTHON_BIN = $(PYTHON_VIRTUAL_ENVIRONMENT)/bin/python$(PYTHON_VERSION)
endif


define quiet
	@if [ "$(VERBOSE)" = "true" ]; then \
		$(1); \
	else \
		$(1) > /dev/null; \
	fi
endef


.PHONY: help
help: # It displays this help message
	@printf "\nUsage: make [COMMAND] [OPTIONS]...\n"
	@awk 'BEGIN {FS = ":.*#"; printf "\nCommands:\n  make \033[36m\033[0m\n"} /^[a-zA-Z_-]+:.*?#/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
	@printf "\nOptions (override with VAR=value):\n"
	@printf "  %-40s %s\n" "VERBOSE=$(VERBOSE)"                   "Show command output (true/false)"
	@printf "  %-40s %s\n" "CI=$(CI)"                       	  "Indicates if the script is running in a CI environment (true/false)"
	@printf "  %-40s %s\n" "PYTHON_VERSION=$(PYTHON_VERSION)"     "Used python interpreter for creating the virtual environment"
	@printf "  %-40s %s\n" "PYTHON_VIRTUAL_ENVIRONMENT=$(PYTHON_VIRTUAL_ENVIRONMENT)" "Name of the virtual environment folder"
	@printf "\n"


.PHONY: setup
setup: # It setups the project, creates the virtual environment and installs the dependencies
	@echo -e "\n⌛ Setting up the project...\n"

	$(call quiet, python$(PYTHON_VERSION) -m venv $(PYTHON_VIRTUAL_ENVIRONMENT))
	$(call quiet, $(PYTHON_BIN) -m pip install --upgrade pip)
	$(call quiet, make install-dev)
	$(call quiet, $(PYTHON_BIN) -m pre_commit install --hook-type pre-commit --hook-type commit-msg)

	@echo -e "\n✅ Run 'source $(PYTHON_VIRTUAL_ENVIRONMENT)/bin/activate' to activate the virtual environment.\n"


.PHONY: install-dev
install-dev: # It installs development dependencies
	@echo -e "\n⌛ Installing development dependencies...\n"

	$(call quiet, $(PYTHON_BIN) -m pip install --requirement requirements_dev.txt)

	@echo -e "\n✅ Development dependencies installed correctly.\n"


.PHONY: install
install: # An alias for 'make install-dev'
	@$(MAKE) --no-print-directory install-dev


.PHONY: install-prod
install-prod: # It installs production dependencies
	@echo -e "\n⌛ Installing production dependencies...\n"

	$(call quiet, $(PYTHON_BIN) -m pip install --requirement requirements.txt)

	@echo -e "\n✅ Production dependencies installed correctly.\n"


.PHONY: format
format: # It automatically formats code
	@echo -e "\n⌛ Formatting project code...\n"

	@$(PYTHON_BIN) -m ruff check $(FULL_SOURCES) --fix-only --config $(CONFIGURATION_FILE)
	@$(PYTHON_BIN) -m ruff format $(FULL_SOURCES) --config $(CONFIGURATION_FILE)


.PHONY: lint
lint: # It automatically lints code
	@echo -e "\n⌛ Linting project code...\n"

	@set -e; \
	mypy_exit=0; \
	ruff_exit=0; \
	$(PYTHON_BIN) -m mypy $(FULL_SOURCES) --txt-report . --config-file $(CONFIGURATION_FILE) || mypy_exit=$$?; \
	$(PYTHON_BIN) -m ruff check $(FULL_SOURCES) --config $(CONFIGURATION_FILE) || ruff_exit=$$?; \
	exit $$(( mypy_exit || ruff_exit ))

 
.PHONY: test
test: # It runs all tests
	@echo -e "\n⌛ Running tests...\n"

	@$(PYTHON_BIN) -m pytest --config-file $(CONFIGURATION_FILE)


.PHONY: tests
tests: # An alias for 'make test'
	@$(MAKE) --no-print-directory test


.PHONY: coverage
coverage: # It gets the test coverage report
	@echo -e "\n⌛ Getting test coverage report...\n"

	@set -e; \
	$(PYTHON_BIN) -m coverage erase; \
	$(PYTHON_BIN) -m coverage run --module pytest --config-file $(CONFIGURATION_FILE) || coverage_exit=$$?; \
	$(PYTHON_BIN) -m coverage combine; \
	$(PYTHON_BIN) -m coverage report; \
	exit $${coverage_exit:-0}


.PHONY: build
build: # It builds the project
	@echo -e "\n⌛ Building project...\n"

	$(call quiet, $(PYTHON_BIN) -m build)

	@echo -e "\n✅ Project built correctly.\n"


.PHONY: audit
audit: # It audits dependencies and source code
	@echo -e "\n⌛ Running security audit...\n"

ifeq ($(CI), true)
	@$(PYTHON_BIN) -m pip_audit --progress-spinner off --requirement requirements_dev.txt
else
	@$(PYTHON_BIN) -m pip_audit --progress-spinner off --requirement requirements_dev.txt
endif

	@echo -e "\n✅ Security audit completed correctly.\n"


.PHONY: clean
clean: # It cleans up the project, removing the virtual environment and some files
	@echo -e "\n⌛ Cleaning up the project...\n"

	$(call quiet, $(PYTHON_BIN) -m pre_commit clean)
	$(call quiet, $(PYTHON_BIN) -m pre_commit uninstall --hook-type pre-commit --hook-type commit-msg)
	$(call quiet, rm --force --recursive $(PYTHON_VIRTUAL_ENVIRONMENT))
	$(call quiet, rm --force --recursive `find . -type f -name '*.py[co]'`)
	$(call quiet, rm --force --recursive `find . -name __pycache__`)
	$(call quiet, rm --force --recursive `find . -name .ruff_cache`)
	$(call quiet, rm --force --recursive `find . -name .mypy_cache`)
	$(call quiet, rm --force --recursive `find . -name .pytest_cache`)
	$(call quiet, rm --force --recursive `find . -name index.txt`)
	$(call quiet, rm --force --recursive .coverage)
	$(call quiet, rm --force --recursive .coverage.*)
	$(call quiet, rm --force --recursive coverage.xml)
	$(call quiet, rm --force --recursive htmlcov)

	@echo -e "\n✅ Run 'deactivate' to deactivate the virtual environment.\n"


.PHONY: update-lists
update-lists: # It updates content lists
	@echo -e "\n⌛ Updating content lists...\n"

	@$(PYTHON_BIN) update_lists.py

	@echo -e "\n✅ Content lists updated correctly.\n"
