from globantchallenge.core.database import engine, Base
from globantchallenge.models.models import Department, Job, HiredEmployee


def init_db():
    Base.metadata.create_all(bind=engine)
