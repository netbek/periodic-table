ifneq ($(shell which tput),)
	ifneq ($(TERM),)
		RED    := $(shell tput setaf 1)
		GREEN  := $(shell tput setaf 2)
		YELLOW := $(shell tput setaf 3)
		CYAN   := $(shell tput setaf 6)
		RESET  := $(shell tput sgr0)
	endif
endif

# ==============================================================================
# DEPENDENCY MANAGEMENT
# ==============================================================================

deps-scan:
	@echo "$(YELLOW)Scanning root lockfiles for vulnerabilities...$(RESET)"
	trivy fs pnpm-lock.yaml --table-mode detailed
	trivy fs uv.lock --table-mode detailed

repo-scan:
	@echo "$(YELLOW)Scanning entire repository for vulnerabilities...$(RESET)"
	trivy fs .

node-outdated:
	@echo "$(YELLOW)Listing outdated Node dependencies...$(RESET)"
	@pnpm outdated || true

node-upgrade: PACKAGE := $(word 2,$(MAKECMDGOALS))
node-upgrade:
	@if [ -z "$(PACKAGE)" ]; then \
		echo "$(YELLOW)Upgrading all Node dependencies...$(RESET)"; \
		pnpm exec ncu --packageManager pnpm --install always; \
	else \
		echo "$(YELLOW)Upgrading '$(PACKAGE)'...$(RESET)"; \
		pnpm exec ncu $(PACKAGE) --packageManager pnpm --install always; \
	fi

# Prevent make from treating arguments to node-upgrade as targets
ifeq (node-upgrade,$(firstword $(MAKECMDGOALS)))
%:
	@:
endif

node-why: PACKAGE := $(word 2,$(MAKECMDGOALS))
node-why:
	@if [ -z "$(PACKAGE)" ]; then \
		echo "$(RED)Error: Package name is required.$(RESET)"; \
		echo "Usage: make node-why <package>"; \
		exit 1; \
	fi
	@echo "$(YELLOW)Listing Node dependencies of '$(PACKAGE)'...$(RESET)"
	pnpm why $(PACKAGE)

# Prevent make from treating arguments to node-why as targets
ifeq (node-why,$(firstword $(MAKECMDGOALS)))
%:
	@:
endif

python-outdated:
	@echo "$(YELLOW)Listing outdated Python dependencies...$(RESET)"
	@uv tree --outdated --depth 1

python-upgrade: PACKAGE := $(word 2,$(MAKECMDGOALS))
python-upgrade:
	@if [ -z "$(PACKAGE)" ]; then \
		echo "$(YELLOW)Upgrading all Python dependencies...$(RESET)"; \
		uv lock --upgrade; \
	else \
		echo "$(YELLOW)Upgrading '$(PACKAGE)'...$(RESET)"; \
		uv lock --upgrade-package $(PACKAGE); \
	fi

# Prevent make from treating arguments to python-upgrade as targets
ifeq (python-upgrade,$(firstword $(MAKECMDGOALS)))
%:
	@:
endif

python-why: PACKAGE := $(word 2,$(MAKECMDGOALS))
python-why:
	@if [ -z "$(PACKAGE)" ]; then \
		echo "$(RED)Error: Package name is required.$(RESET)"; \
		echo "Usage: make python-why <package>"; \
		exit 1; \
	fi
	@echo "$(YELLOW)Listing Python dependencies of '$(PACKAGE)'...$(RESET)"
	uv tree --invert --package $(PACKAGE)

# Prevent make from treating arguments to python-why as targets
ifeq (python-why,$(firstword $(MAKECMDGOALS)))
%:
	@:
endif

uv-sync:
	uv sync --all-extras --all-groups

# ==============================================================================
# FORMAT
# ==============================================================================

format:
	@echo "Formatting code..."
	pre-commit run prettier-js --all-files
	pre-commit run pyupgrade --all-files
	pre-commit run isort --all-files
	pre-commit run ruff-format --all-files

# ==============================================================================
# LINT & TEST
# ==============================================================================

lint:
	@echo "Linting code..."
	pre-commit run ruff-check --hook-stage manual --all-files

# ==============================================================================
# PUBLISH
# ==============================================================================

bump-version:
	@BUMP=$(word 2,$(MAKECMDGOALS)); \
	VALID_BUMP="major minor patch"; \
	if [ -z "$$BUMP" ]; then \
		echo "$(RED)Error: Bump is required.$(RESET)"; \
		echo "Usage: make bump-version [major|minor|patch]"; \
		exit 1; \
	fi; \
	if ! echo "$$VALID_BUMP" | grep -qw "$$BUMP"; then \
		echo "$(RED)Error: Invalid bump '$$BUMP'.$(RESET)"; \
		echo "Must be one of: $(CYAN)$$VALID_BUMP$(RESET)"; \
		exit 1; \
	fi; \
	pnpm version $$BUMP; \
	uv version --bump $$BUMP; \
	VERSION=$$(uv version --short); \
	git add \
		pyproject.toml \
		uv.lock; \
	git commit -m $$VERSION;

build:
	python python/dump.py
	gulp
	find python/dist -maxdepth 1 ! -name ".gitignore" -type f -exec rm -f {} +
	uv build -o python/dist --sdist
	uv build -o python/dist --wheel
	twine check python/dist/*

build-and-commit:
	@VERSION=$$(uv version --short); \
	$(MAKE) --no-print-directory build; \
	git add data demo; \
	git commit -m "Build $$VERSION";

create-release:
	@VERSION=$$(uv version --short); \
	gh release create $$VERSION; \
	git fetch --tags;

publish:
	@PASSWORD=$$(keyring get pypi-chrys __token__); \
	if [ -z "$$PASSWORD" ]; then \
		echo "$(RED)Error: PyPI token not found in keyring. Run: keyring set pypi-chrys __token__$(RESET)"; \
		exit 1; \
	fi; \
	TWINE_USERNAME=__token__ TWINE_PASSWORD="$$PASSWORD" twine upload --verbose dist/*; \
	pnpm publish

deploy:
	node scripts/deploy.js

# Prevent make from treating arguments to bump-version as targets
ifeq (bump-version,$(firstword $(MAKECMDGOALS)))
%:
	@:
endif
