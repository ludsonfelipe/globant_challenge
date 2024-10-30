from io import BytesIO
import pytest
from fastapi import status


def test_upload_employees_success(client):
    csv_content = b"1,John Doe,2021-11-07T02:48:42Z,1,1"
    files = {"file": ("employees.csv", BytesIO(csv_content), "text/csv")}

    response = client.post("/upload/employees/", files=files)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "Dados de empregados carregados com sucesso"}


def test_upload_departments_success(client):
    csv_content = b"1,IT"
    files = {"file": ("departments.csv", BytesIO(csv_content), "text/csv")}

    response = client.post("/upload/departments/", files=files)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "status": "Dados de departamentos carregados com sucesso"
    }


def test_upload_jobs_success(client):
    csv_content = b"1,Developer"
    files = {"file": ("jobs.csv", BytesIO(csv_content), "text/csv")}

    response = client.post("/upload/jobs/", files=files)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "Dados de empregos carregados com sucesso"}


def test_upload_invalid_batch_size(client):
    csv_content = b"1,Developer"
    files = {"file": ("jobs.csv", BytesIO(csv_content), "text/csv")}

    response = client.post("/upload/jobs/?batch_size=1001", files=files)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "Batch size must be between 1 and 1000"


def test_upload_invalid_csv(client):
    files = {"file": ("jobs.csv", BytesIO(b"invalid,csv,format"), "text/csv")}

    response = client.post("/upload/jobs/", files=files)

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert "Error reading csv file" in response.json()["detail"]
