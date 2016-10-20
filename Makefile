# OpenBikes API Makefile

## Configuration

PACKAGE    := "obpy"
BUILD_TIME := $(shell date +%FT%T%z)
PROJECT    := $(shell basename $(PWD))

## Commands

.PHONY: all
all: install 

# Install dependencies
.PHONY: install
install:
	pip3 install -r requirements.txt

# Launch test suite
.PHONY: test
test:
	pytest --verbose --cov=$(PACKAGE) tests/