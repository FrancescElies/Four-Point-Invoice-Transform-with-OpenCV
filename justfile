init: clean-build
  rm -rf venv
  python3.9 -m venv venv
  . venv/bin/activate
  pip install --upgrade wheel pip setuptools
  pip install --upgrade -r requirements/main.txt  -r requirements/dev.txt
  pip install --editable .
  echo run . venv/bin/activate to activate venv

clean-build:
  rm -rf build/
  rm -rf .tox
  rm -rf .pytest_cache
  rm -rf dist/
  rm -rf *.egg-info

update-deps:
  pip install --upgrade pip-tools
  pip-compile --upgrade --build-isolation --generate-hashes --output-file requirements/main.txt requirements/main.in
  pip-compile --upgrade --build-isolation --generate-hashes --output-file requirements/dev.txt requirements/dev.in

build: clean-build
	python -m pip install --upgrade --quiet setuptools wheel twine
	python setup.py sdist bdist_wheel
	tox -e packaging -- -o dist/pex-$(uname)/image-to-scan

publish-pypi: build
	python -m twine check dist/*
	python -m twine upload dist/*

publish-testpypi: build
	python -m twine check dist/*
	python -m twine upload --repository testpypi dist/*

test: lint
	tox -e venv

lint:
	flake8 image_to_scan