from pydantic import BaseModel


class DepartmentCreate(BaseModel):
    id: int
    department: str

    class Config:
        orm_mode = True
