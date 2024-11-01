from pydantic import BaseModel


class DepartmentCreate(BaseModel):
    id: int
    department: str

    class Config:
        from_attributes = True
