.PHONY: install validate test serve build verify-site check sources

install:
	python -m pip install --require-hashes -r requirements.txt

validate:
	python scripts/validate.py

test:
	pytest

serve:
	mkdocs serve

build:
	mkdocs build --strict

verify-site: build
	python scripts/verify_site.py

sources:
	python scripts/check_external_links.py

check: validate test verify-site
