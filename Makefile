ifneq ($(shell which tput),)
	ifneq ($(TERM),)
		RED    := $(shell tput setaf 1)
		GREEN  := $(shell tput setaf 2)
		YELLOW := $(shell tput setaf 3)
		CYAN   := $(shell tput setaf 6)
		RESET  := $(shell tput sgr0)
	endif
endif

lint:
	@echo "Linting code..."
	pre-commit run ruff-check --hook-stage manual --all-files

format:
	@echo "Formatting code..."
	pre-commit run prettier-js --all-files
	pre-commit run pyupgrade --all-files
	pre-commit run isort --all-files
	pre-commit run ruff-format --all-files

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
	npm version $$BUMP; \
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
	gh release create $$VERSION;

publish:
	npm publish
	twine upload --config-file .pypirc --verbose python/dist/*

deploy:
	node scripts/deploy.js

# Prevent make from treating arguments to bump-version as targets
ifeq (bump-version,$(firstword $(MAKECMDGOALS)))
%:
	@:
endif
