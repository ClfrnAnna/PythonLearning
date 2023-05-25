from fastapi import APIRouter, Depends, status, HTTPException
from pydantic import parse_obj_as
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.db.session import get_session
from app.queries import select_all_tasks, insert_task, select_task_by_id, update_task, delete_task
from app.schemas import TasksSchema, TaskSchema, TaskCreationSchema, TaskChangeSchema

tasks_router = APIRouter(prefix="/api", tags=["Tasks"])


@tasks_router.get("/tasks")
def get_all_tasks_api(session: Session = Depends(get_session)) -> TasksSchema:
    tasks = select_all_tasks(session)

    return TasksSchema(tasks=parse_obj_as(list[TaskSchema], tasks))


@tasks_router.post("/tasks", status_code=status.HTTP_201_CREATED, response_model=TaskSchema)
def create_task_api(task: TaskCreationSchema, session: Session = Depends(get_session)):
    task = insert_task(session, task)

    return task


@tasks_router.get("/tasks/{task_id}", response_model=TaskSchema)
def get_task_api(task_id: int, session: Session = Depends(get_session)):
    try:
        task = select_task_by_id(session, task_id)
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Task № {task_id} doesn't exist"
        )

    return task


@tasks_router.patch("/tasks/{task_id}", response_model=TaskSchema)
def edit_task_api(task_id: int, task_change: TaskChangeSchema, session: Session = Depends(get_session)):
    try:
        task = update_task(session, task_id, task_change)
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Task № {task_id} doesn't exist"
        )

    return task


@tasks_router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task_api(task_id: int, session: Session = Depends(get_session)):
    delete_task(session, task_id)
