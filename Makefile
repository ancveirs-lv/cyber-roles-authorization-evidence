.PHONY: install generate generate-check validate test serve build verify-site check sources

install:
	python -m pip install --require-hashes -r requirements.txt

validate:
	python scripts/validate.py

generate:
	python scripts/generate_glossary.py

generate-check:
	python scripts/generate_glossary.py --check

test:
	pytest

serve:
	mkdocs serve

build:
	mkdocs build --strict
	python scripts/postprocess_site.py

verify-site: build
	python scripts/verify_site.py

sources:
	python scripts/check_external_links.py

check: generate-check validate test verify-site
