from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
import polars as pl
from globantchallenge.core.database import get_db
from globantchallenge.models.models import HiredEmployee, Department, Job
from globantchallenge.schemas.employee import EmployeeCreate
from globantchallenge.schemas.department import DepartmentCreate
from globantchallenge.schemas.job import JobCreate

router = APIRouter()


@router.post("/upload/employees/")
async def upload_employees_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    batch_size: int = 1000,
):
    try:
        df = pl.read_csv(file.file, has_header=False)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading csv file: {e}")

    if batch_size < 1 or batch_size > 1000:
        raise HTTPException(
            status_code=400, detail="Batch size must be between 1 and 1000"
        )

    df.columns = ["id", "name", "datetime", "department_id", "job_id"]

    employees = df.to_struct("employee")

    for employee_data in range(0, len(employees), batch_size):
        batch = employees[employee_data : employee_data + batch_size]

        employees = [
            HiredEmployee(**EmployeeCreate(**record).model_dump()) for record in batch
        ]

        db.bulk_save_objects(employees)

    db.commit()
    return {"status": "Dados de empregados carregados com sucesso"}


@router.post("/upload/departments/")
async def upload_departments_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    batch_size: int = 1000,
):
    try:
        df = pl.read_csv(file.file, has_header=False)
        df.columns = ["id", "department"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading csv file: {e}")

    if batch_size < 1 or batch_size > 1000:
        raise HTTPException(
            status_code=400, detail="Batch size must be between 1 and 1000"
        )

    departments = df.to_struct("department")

    for department_data in range(0, len(departments), batch_size):
        batch = departments[department_data : department_data + batch_size]

        departments = [
            Department(**DepartmentCreate(**record).model_dump()) for record in batch
        ]

        db.bulk_save_objects(departments)

    db.commit()
    return {"status": "Dados de departamentos carregados com sucesso"}


@router.post("/upload/jobs/")
async def upload_jobs_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    batch_size: int = 1000,
):
    try:
        df = pl.read_csv(file.file, has_header=False)
        df.columns = ["id", "job"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading csv file: {e}")

    if batch_size < 1 or batch_size > 1000:
        raise HTTPException(
            status_code=400, detail="Batch size must be between 1 and 1000"
        )

    jobs = df.to_struct("job")

    for job_data in range(0, len(jobs), batch_size):
        batch = jobs[job_data : job_data + batch_size]

        jobs = [Job(**JobCreate(**record).model_dump()) for record in batch]

        db.bulk_save_objects(jobs)

    db.commit()
    return {"status": "Dados de empregos carregados com sucesso"}
