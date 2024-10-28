run-api:
	uvicorn globantchallenge.main:app

### Development
sort-imports:
	isort .

format:
	black .

lint:
	ruff check .

test:
	pytest -v tests/ 

test-coverage:
	pytest --cov=globantchallenge tests/

CI:
	make sort-imports
	make format
	make lint
	make test
