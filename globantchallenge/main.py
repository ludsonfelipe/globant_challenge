from fastapi import FastAPI
from globantchallenge.api.endpoints import upload, queries
from globantchallenge.core.init_db import init_db

app = FastAPI()

init_db()

app.include_router(upload.router, tags=["upload"])
app.include_router(queries.router, tags=["queries"])
