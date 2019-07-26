.PHONY: init update-dependencies clean-build dist publish lint test

update-dependencies:
	pip-compile requirements/dev.in
	pip-compile --output-file requirements/main.txt
	pip install --upgrade -r requirements/main.txt

init:
	python3.7 -m virtualenv venv
	source venv/bin/activate; pip install --upgrade -r requirements/main.txt
	pip install --upgrade -r requirements/dev.txt
	source venv/bin/activate; pip install --editable .

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

build: clean-build
	python -m pip install --upgrade --quiet setuptools wheel twine
	python setup.py sdist bdist_wheel

publish-pypi: build
	python -m twine check dist/*
	python -m twine upload dist/*

publish-testpypi: build
	python -m twine check dist/*
	python -m twine upload --repository testpypi dist/*

test: lint
	tox -e ALL

lint:
	flake8 image_to_scan
