#!/usr/bin/env bash

set -ex

PYTHONPATH=. exec pipenv run python3 setup.py test

