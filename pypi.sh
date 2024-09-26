[[ ! -d venv ]] && python3 -m venv venv && ./venv/bin/pip install setuptools wheel twine black

pydoc-markdown > DOCS.md
./venv/bin/black .
./venv/bin/python setup.py sdist bdist_wheel
./venv/bin/twine upload dist/*

rm -rf build dist