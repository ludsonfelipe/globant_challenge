from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EmployeeCreate(BaseModel):
    id: int
    name: Optional[str] = None
    datetime: Optional[str] = None
    department_id: Optional[int] = None
    job_id: Optional[int] = None

    class Config:
        orm_mode = True
