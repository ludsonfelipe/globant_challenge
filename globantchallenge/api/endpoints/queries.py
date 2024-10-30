from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import Float
from sqlalchemy import func, case
from globantchallenge.core.database import get_db
from globantchallenge.models.models import HiredEmployee, Department, Job

router = APIRouter()


@router.get("/employees/hired_per_quarter/")
def get_employees_hired_per_quarter(
    year: int = Query(2021, description="Year to filter the hired employees by"),
    db: Session = Depends(get_db),
):
    results = (
        db.query(
            Department.department.label("department"),
            Job.job.label("job"),
            func.sum(
                case((func.extract("quarter", HiredEmployee.datetime) == 1, 1), else_=0)
            ).label("Q1"),
            func.sum(
                case((func.extract("quarter", HiredEmployee.datetime) == 2, 1), else_=0)
            ).label("Q2"),
            func.sum(
                case((func.extract("quarter", HiredEmployee.datetime) == 3, 1), else_=0)
            ).label("Q3"),
            func.sum(
                case((func.extract("quarter", HiredEmployee.datetime) == 4, 1), else_=0)
            ).label("Q4"),
        )
        .join(Job, Job.id == HiredEmployee.job_id, isouter=True)
        .join(Department, Department.id == HiredEmployee.department_id, isouter=True)
        .filter(func.extract("year", HiredEmployee.datetime) == year)
        .group_by(Department.department, Job.job)
        .order_by(Department.department, Job.job)
        .all()
    )
    print(results)
    return [
        {
            "department": row.department,
            "job": row.job,
            "Q1": row.Q1,
            "Q2": row.Q2,
            "Q3": row.Q3,
            "Q4": row.Q4,
        }
        for row in results
    ]


@router.get("/departments/above_average_hired/")
def get_departments_above_average_hired(
    year: int = Query(2021, description="Year to filter the hired employees by"),
    db: Session = Depends(get_db),
):
    subquery = (
        db.query(
            (func.count(HiredEmployee.id) / func.count(Department.id.distinct())).cast(
                Float
            )
        )
        .select_from(HiredEmployee)
        .join(Department, HiredEmployee.department_id == Department.id)
        .filter(func.extract("year", HiredEmployee.datetime) == year)
        .scalar_subquery()
    )

    results = (
        db.query(
            Department.id,
            Department.department.label("department"),
            func.count(HiredEmployee.id).label("hired"),
        )
        .join(HiredEmployee, HiredEmployee.department_id == Department.id, isouter=True)
        .group_by(Department.id, Department.department)
        .having(func.count(HiredEmployee.id) > subquery)
        .order_by(func.count(HiredEmployee.id).desc())
        .all()
    )

    return [
        {
            "id": row.id,
            "department": row.department,
            "hired": row.hired,
        }
        for row in results
    ]
