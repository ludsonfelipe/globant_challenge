# Docker
docker-build:
	docker build -t globant-api .

docker-run-local:
	docker run -p 8000:8000 globant-api

test-api-cloud:
	curl -X POST -F "file=@data/jobs.csv" $(url)

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

infra_plan:
	terraform -chdir=./terraform plan

infra_apply:
	terraform -chdir=./terraform apply -auto-approve

infra_destroy:
	terraform -chdir=./terraform destroy -auto-approve

#### Cloud Build
infra_cloudbuild_apply:
	terraform -chdir=./terraform apply -target module.cloud_build

infra_cloudbuild_destroy:
	terraform -chdir=./terraform destroy -target module.cloud_build

#### Artifact Registry
infra_artifactregistry_apply:
	terraform -chdir=./terraform apply -target module.artifact_registry

infra_artifactregistry_destroy:
	terraform -chdir=./terraform destroy -target module.artifact_registry

