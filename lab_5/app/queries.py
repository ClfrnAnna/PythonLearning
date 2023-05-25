from typing import Sequence

from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session

from app.db.models import Task
from app.schemas import TaskCreationSchema, TaskChangeSchema


def select_all_tasks(session: Session) -> Sequence[Task]:
    stmt = select(Task)

    return session.scalars(stmt).all()


def select_task_by_id(session: Session, task_id: int) -> Task:
    stmt = select(Task).where(Task.id == task_id)

    return session.scalars(stmt).one()


def insert_task(session: Session, task: TaskCreationSchema) -> Task:
    stmt = insert(Task).values(task.dict()).returning(Task)
    task = session.scalars(stmt).one()
    session.commit()

    return task


def update_task(session: Session, task_id: int, task_change: TaskChangeSchema) -> Task:
    stmt = update(Task).where(Task.id == task_id).values(task_change.dict(exclude_unset=True)).returning(Task)

    return session.scalars(stmt).one()


def delete_task(session: Session, task_id: int) -> None:
    stmt = delete(Task).where(Task.id == task_id)

    session.execute(stmt)
    session.commit()
