# Use a imagem oficial do Python como base
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Instala o poetry
RUN pip install poetry

# Copia os arquivos de configuração do poetry
COPY pyproject.toml poetry.lock ./

# Configura o poetry para não criar um ambiente virtual
RUN poetry config virtualenvs.create false

# Instala as dependências
RUN poetry install --no-dev --no-interaction --no-ansi

# Copia o código da aplicação
COPY globantchallenge/ ./globantchallenge/

# Expõe a porta que a aplicação usará
EXPOSE 8000

# Comando para executar a aplicação
CMD ["uvicorn", "globantchallenge.main:app", "--host", "0.0.0.0", "--port", "8000"]