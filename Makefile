run-api:
	uvicorn globantchallenge.main:app

### Development
sort-imports:
	poetry run isort .

format:
	poetry run black .

lint:
	poetry run ruff check .

test:
	poetry run pytest -v tests/ 

test-coverage:
	poetry run pytest --cov=globantchallenge tests/

CI:
	make sort-imports
	make format
	make lint
	make test

### Terraform
infra:
	terraform -chdir=./terraform init

infra_apply:
	terraform -chdir=./terraform apply -auto-approve

