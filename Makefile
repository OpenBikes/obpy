# OpenBikes API Makefile

## Configuration

BUILD_TIME := $(shell date +%FT%T%z)
PROJECT    := $(shell basename $(PWD))

## Commands

.PHONY: all
all: install 

# Install dependencies
.PHONY: install
install:
	pip3 install -r requirements.txt

### Setup developpement environment
.PHONY: dev
dev:
	cp config_dev.py config.py

### Setup production environment
.PHONY: prod
prod:
	cp config_prod.py config.py
