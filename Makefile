.PHONY: install validate test serve build check

install:
	python -m pip install -r requirements.txt

validate:
	python scripts/validate.py

test:
	pytest

serve:
	mkdocs serve

build:
	mkdocs build --strict

check: validate test build
