SHELL = /bin/bash

# To see all colors, run
# bash -c 'for c in {0..255}; do tput setaf $c; tput setaf $c | cat -v; echo =$c; done'
# The first 15 entries are the 8-bit colors

# Define standard colors
ifneq (,$(findstring xterm,${TERM}))
	BLACK        := $(shell tput -Txterm setaf 0)
	RED          := $(shell tput -Txterm setaf 1)
	GREEN        := $(shell tput -Txterm setaf 2)
	YELLOW       := $(shell tput -Txterm setaf 3)
	LIGHTPURPLE  := $(shell tput -Txterm setaf 4)
	PURPLE       := $(shell tput -Txterm setaf 5)
	BLUE         := $(shell tput -Txterm setaf 6)
	WHITE        := $(shell tput -Txterm setaf 7)
	RESET := $(shell tput -Txterm sgr0)
else
	BLACK        := ""
	RED          := ""
	GREEN        := ""
	YELLOW       := ""
	LIGHTPURPLE  := ""
	PURPLE       := ""
	BLUE         := ""
	WHITE        := ""
	RESET        := ""
endif

# Set the target color
TARGET_COLOR := $(BLUE)

# Variables
POUND = \#

# Help commands
.PHONY: no_targets__ help
	no_targets__:

.DEFAULT_GOAL := help

colors:  ## Show all the colors
	@echo "${BLACK}BLACK${RESET}"
	@echo "${RED}RED${RESET}"
	@echo "${GREEN}GREEN${RESET}"
	@echo "${YELLOW}YELLOW${RESET}"
	@echo "${LIGHTPURPLE}LIGHTPURPLE${RESET}"
	@echo "${PURPLE}PURPLE${RESET}"
	@echo "${BLUE}BLUE${RESET}"
	@echo "${WHITE}WHITE${RESET}"

help:  ## Show this help
	@echo ""
	@echo "    ${BLACK}:: ${RED}Let-it-go-backend Make Commands${RESET} ${BLACK}::${RESET}"
	@printf -- "${BLACK}-%.0s${RESET}" {1..88}
	@printf "\n"
	@grep -E '^[a-zA-Z_0-9%-]+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "${TARGET_COLOR}%-30s${RESET} %s\n", $$1, $$2}'


# Main Commands
.PHONY: init install install-dev run migrations apply-migrations app

init: migrations apply-migrations install-dev  ## Initialize the database
	python -m let_it_go_backend.manage create_default_admin

install:  ## Install dependencies
	pip install -e .

install-dev:  ## Install dev dependencies
	pip install -e ".[dev]"

server: ## Run the Django Server
	python -m let_it_go_backend.manage runserver

migrations: ## Create migration files
	python -m let_it_go_backend.manage makemigrations

apply-migrations: ## Apply migrations
	python -m let_it_go_backend.manage migrate

app: ## Create a django app
	mkdir -p let_it_go_backend/apps/$(name)
	python -m let_it_go_backend.manage startapp $(name) let_it_go_backend/apps/$(name)


# vim:noexpandtab:ts=8:sw=8:ai
