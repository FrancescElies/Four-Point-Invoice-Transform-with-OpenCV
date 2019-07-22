update-dependencies:
	pip-compile --output-file requirements/main.txt
	pip install --upgrade -r requirements/main.txt

install--pip-tools:
	pip install pip-tools

init:
	python3.7 -m virtualenv .venv
	source .venv/bin/activate; pip install --upgrade -r requirements/main.txt
	source .venv/bin/activate; pip install --editable .

.PHONY: init update-dependencies
