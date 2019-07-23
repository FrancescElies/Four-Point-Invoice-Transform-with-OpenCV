.PHONY: init update-dependencies clean-build dist

update-dependencies:
	pip-compile requirements/dev.in
	pip-compile --output-file requirements/main.txt
	pip install --upgrade -r requirements/main.txt

install--dev-dependencies:
	pip install --upgrade -r requirements/dev.txt

init:
	python3.7 -m virtualenv .venv
	source .venv/bin/activate; pip install --upgrade -r requirements/main.txt
	source .venv/bin/activate; pip install --editable .

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

dist: clean-build
	python3 setup.py sdist bdist_wheel

upload-dist: dist
	twine upload dist/*
