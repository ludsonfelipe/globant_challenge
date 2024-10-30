# globant_challenge# Globant Challenge - Data Migration API

Este projeto é uma solução para um desafio que envolve a criação de uma API para migração de dados e consultas em banco de dados. A aplicação foi desenvolvida usando FastAPI e SQLAlchemy, com suporte para Docker e deploy na Google Cloud Platform.

## 🏗️ Arquitetura

O projeto segue uma arquitetura em camadas:

```
globantchallenge/
├── api/
│   └── endpoints/         # Endpoints da API
├── core/                  # Configurações centrais
├── models/               # Modelos SQLAlchemy
└── schemas/              # Schemas Pydantic
```

## 🚀 Principais Funcionalidades

### 1. Upload de Dados
A API possui três endpoints para upload de dados via CSV:

- `/upload/employees/` - Upload de dados de funcionários
- `/upload/departments/` - Upload de dados de departamentos
- `/upload/jobs/` - Upload de dados de cargos

Características:
- Processamento em lotes (batch_size configurável até 1000 registros)
- Validação de dados usando Pydantic
- Tratamento de erros robusto

### 2. Endpoints de Consulta

#### Funcionários por Trimestre
```
GET /employees/hired_per_quarter/
```
Retorna o número de funcionários contratados por trimestre, agrupados por departamento e cargo.

#### Departamentos Acima da Média
```
GET /departments/above_average_hired/
```
Lista departamentos que contrataram mais funcionários que a média no ano especificado.

## 🛠️ Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e rápido
- **SQLAlchemy**: ORM para interação com banco de dados
- **Polars**: Biblioteca para processamento eficiente de dados
- **Docker**: Containerização
- **PostgreSQL**: Banco de dados (configurável via Docker Compose)
- **Terraform**: Infraestrutura como código
- **Google Cloud Platform**: Plataforma de deploy

## 🔧 Configuração do Ambiente

1. Clone o repositório
2. Configure as variáveis de ambiente:
```bash
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_DB=nome_do_banco
```

3. Inicie os containers:
```bash
docker-compose up -d
```

## 🚀 Deploy

O projeto inclui configuração Terraform para deploy na GCP, incluindo:
- Cloud Build
- Artifact Registry
- Cloud Run

Para fazer deploy:
```bash
make infra
make infra_plan
make infra_apply
```

## 🧪 Testes

O projeto inclui testes unitários e de integração. Para executar:
```bash
make test
```

Para verificar a cobertura:
```bash
make test-coverage
```

## 🔍 Qualidade de Código

O projeto utiliza várias ferramentas para garantir a qualidade do código:
```bash
make sort-imports  # Organiza imports
make format       # Formata código (black)
make lint         # Verifica estilo (ruff)
```

## 📝 Licença

Este projeto está sob a licença MIT.