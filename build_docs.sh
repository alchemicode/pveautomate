#!/usr/bin/env bash

# Create the _site directory if it doesn't exist
mkdir -p _site

[[ ! -d venv ]] && python3 -m venv venv

./venv/bin/pip install -r requirements.txt

./venv/bin/python -m pydoc -w pveautomate/automate.py

mv automate.html _site/index.html

echo "HTML documentation has been generated in the _site directory."
