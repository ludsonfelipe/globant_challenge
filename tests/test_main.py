from io import BytesIO

from fastapi import status
from fastapi.testclient import TestClient

from globantchallenge.main import app

client = TestClient(app)


def test_upload_csv_success():
    # Cria um arquivo CSV fictício para teste
    fake_csv = BytesIO(b"header1,header2\nvalue1,value2")
    files = {"file": ("test.csv", fake_csv, "text/csv")}

    response = client.post("/upload-csv/", files=files)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"filename_": "test.csv"}


def test_upload_csv_no_file():
    response = client.post("/upload-csv/")

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_upload_csv_empty_file():
    files = {"file": ("test.csv", BytesIO(b""), "text/csv")}

    response = client.post("/upload-csv/", files=files)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"filename_": "test.csv"}
