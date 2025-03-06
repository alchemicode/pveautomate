#!/usr/bin/env bash

set -e

[[ ! -d venv ]] && python3 -m venv venv
./venv/bin/pip install --upgrade setuptools wheel twine black pydoc-markdown

./venv/bin/pydoc-markdown > DOCS.md
./venv/bin/black .
./venv/bin/python setup.py sdist bdist_wheel
unset DBUS_SESSION_BUS_ADDRESS
./venv/bin/twine upload dist/*

rm -rf build dist