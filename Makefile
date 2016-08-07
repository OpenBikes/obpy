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