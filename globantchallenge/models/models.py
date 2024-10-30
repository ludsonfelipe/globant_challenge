from sqlalchemy import Column, Integer, String, DateTime
from globantchallenge.core.database import Base


class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    department = Column(String, index=True)


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    job = Column(String, index=True)


class HiredEmployee(Base):
    __tablename__ = "hired_employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    datetime = Column(DateTime, nullable=True)
    department_id = Column(Integer, nullable=True)
    job_id = Column(Integer, nullable=True)
