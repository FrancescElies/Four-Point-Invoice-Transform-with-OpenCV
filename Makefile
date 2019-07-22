update-dependencies:
	pip-compile requirements/main.in

init:
	python3.7 -m virtualenv .venv
	source .venv/bin/activate; pip install --upgrade -r requirements/main.txt

.PHONY: init update-dependencies
