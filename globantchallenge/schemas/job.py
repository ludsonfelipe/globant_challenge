from pydantic import BaseModel


class JobCreate(BaseModel):
    id: int
    job: str

    class Config:
        orm_mode = True
