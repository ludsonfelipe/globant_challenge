from datetime import datetime
from globantchallenge.models.models import Department, Job, HiredEmployee


def test_department_model():
    department = Department(id=1, department="IT")
    assert department.id == 1
    assert department.department == "IT"


def test_job_model():
    job = Job(id=1, job="Developer")
    assert job.id == 1
    assert job.job == "Developer"


def test_hired_employee_model():
    employee = HiredEmployee(
        id=1, name="John Doe", datetime=datetime(2021, 1, 1), department_id=1, job_id=1
    )
    assert employee.id == 1
    assert employee.name == "John Doe"
    assert employee.datetime == datetime(2021, 1, 1)
    assert employee.department_id == 1
    assert employee.job_id == 1
