format:
	uv run black .

lint: ruff mypy pyright

mypy:
	uv run mypy --ignore-missing-imports .

pyright:
	uv run pyright

ruff:
	uv run ruff check

test:
	uv run pytest -s ./tests/**

test-coverage:
	uv run pytest \
		--cov-config=.coveragerc \
		--cov-report=term \
		--cov-report=html \
		--cov-report=xml \
		--no-cov-on-fail \
		--cov=. \
		-s ./tests/**

run:
	uv run uvicorn src.main:app --host 0.0.0.0 --port 8080