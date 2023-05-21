from typing import Sequence

from sqlalchemy import select, update, func, cast, case, Float
from sqlalchemy.orm import Session

from lab3.models import Task, Lesson, Student, Group


def select_tasks_by_theme(session: Session, theme: str) -> Sequence[Task]:
    stmt = select(Task).join(Lesson, Lesson.id == Task.lesson_id).where(Lesson.theme == theme)

    tasks = session.scalars(stmt).all()

    return tasks


def select_tasks_by_difficulty_lvl(session: Session, lvl: int) -> Sequence[Task]:
    stmt = select(Task).where(Task.difficulty_level == lvl)

    return session.scalars(stmt).all()


def select_student_tasks_by_status(session: Session, status: str, student_id: int) -> Sequence[Task]:
    stmt = select(Task).join(
        Student, Student.id == Task.student_id
    ).where(
        Student.id == student_id
    ).where(
        Task.status == status
    )

    session.execute(stmt)

    return session.scalars(stmt).all()


def select_all_student_tasks(session: Session, student_id: int) -> Sequence[Task]:
    stmt = select(Task).join(Student, Student.id == Task.student_id).where(Student.id == student_id)

    return session.scalars(stmt).all()


def select_group_students_by_teacher(
    session: Session, group_id: int, teacher_id: int, lesson_id: int
) -> Sequence[Student]:
    stmt = select(Student).join(
        Group, Group.id == Student.group_id
    ).join(
        Lesson, Group.id == Lesson.group_id
    ).where(
        Group.id == group_id
    ).where(
        Lesson.teacher_id == teacher_id
    ).where(
        Lesson.id == lesson_id
    )

    return session.scalars(stmt).all()


def update_student_task_status(session: Session, task_id: int, student_id: int, status: str) -> None:
    stmt = update(Task).where(Task.student_id == student_id).where(Task.id == task_id).values(status=status)
    session.execute(stmt)


def get_solved_tasks_percentage(session: Session) -> float:
    stmt = select(
        ((func.sum(case((Task.status == "SOLVED", 1), else_=0)) / cast(func.count(), Float)) * 100).label("percentage")
    ).select_from(Task)

    row = session.execute(stmt).fetchone()

    return row.percentage


def get_group_academic_performance_percentage(session: Session, group_id: int) -> float:
    stmt = select(
        ((func.sum(case((Task.status == "SOLVED", 1), else_=0)) / cast(func.count(), Float)) * 100).label("percentage")
    ).select_from(Task).join(
        Student, Student.id == Task.student_id
    ).where(Student.group_id == group_id)

    row = session.execute(stmt).fetchone()

    return row.percentage


def get_group_name(session: Session, group_id: int) -> str:
    stmt = select(Group.name).where(Group.id == group_id)

    return session.execute(stmt).one().name
