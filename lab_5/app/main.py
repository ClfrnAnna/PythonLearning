from fastapi import FastAPI

from app.tasks import tasks_router

app = FastAPI(title="Education")


app.include_router(tasks_router)
