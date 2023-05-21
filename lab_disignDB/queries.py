from typing import Sequence

from sqlalchemy import Row, select, or_, func
from sqlalchemy.orm import Session

from lab_disignDB.models import Employee, JobTitle, Vacation, FormerJob


def select_employee_in_vacation(session: Session) -> Sequence[Row]:
    stmt = (
        select(Employee.name, JobTitle.job, JobTitle.salary)
        .select_from(Employee)
        .join(JobTitle, JobTitle.id == Employee.job_title_id)
        .join(Vacation, Employee.id == Vacation.employee_id)
        .where(or_(Employee.child == True, Employee.retiree == True))
        .where(func.current_date().between(Vacation.data_from, Vacation.data_to))
    )

    return session.execute(stmt).fetchall()


def select_employee_position(session: Session) -> Sequence[Row]:
    stmt = select(Employee.id, Employee.name, JobTitle.job).select_from(Employee).join(
        JobTitle, JobTitle.id == Employee.job_title_id
    )

    return session.execute(stmt).fetchall()


def select_employees_former_jobs(session: Session) -> Sequence[Row]:
    stmt = (
        select(Employee.id, Employee.name, FormerJob, )
        .select_from(FormerJob)
        .join(Employee, Employee.id == FormerJob.employee_id)
    )

    return session.execute(stmt).fetchall()


def search_employee(session: Session, name: str) -> Employee:
    stmt = select(Employee).where(Employee.name == name)

    return session.scalars(stmt).one()
