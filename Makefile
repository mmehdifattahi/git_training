run:
	python src/main.py

test:
	pytest

lint:
	ruff check src tests
