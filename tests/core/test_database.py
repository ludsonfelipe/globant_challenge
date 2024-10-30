from sqlalchemy.orm import Session
from globantchallenge.core.database import get_db


def test_get_db():
    db_generator = get_db()
    db = next(db_generator)
    assert isinstance(db, Session)
    try:
        next(db_generator)
    except StopIteration:
        pass
