import datetime

from sqlalchemy import insert
from sqlalchemy.orm import Session

from lab_disignDB.models import CategorysVacation, JobTitle, Employee, Vacation, FormerJob


def insert_vacation_category(session: Session, category_name: str) -> None:
    stmt = insert(CategorysVacation).values(name=category_name)

    session.execute(stmt)


def insert_job_title(session: Session, job: str, salary: int) -> None:
    stmt = insert(JobTitle).values(job=job, salary=salary)

    session.execute(stmt)


def insert_employee(
    session: Session,
    name: str,
    dob: datetime.date,
    child: bool,
    disability: bool,
    retiree: bool,
    job_title_id: int,
) -> None:
    stmt = insert(Employee).values(
        name=name, dob=dob, child=child, disability=disability, retiree=retiree, job_title_id=job_title_id
    )
    session.execute(stmt)


def insert_vacation(
    session: Session,
    data_from: datetime.date,
    data_to: datetime.date,
    employee_id: int,
    categorys_vacation_id: int,
) -> None:
    stmt = insert(Vacation).values(
        data_from=data_from,
        data_to=data_to,
        employee_id=employee_id,
        categorys_vacation_id=categorys_vacation_id
    )

    session.execute(stmt)


def insert_former_job(
   session: Session,
   name: str,
   job_title: str,
   term: int,
   date_start: datetime.date,
   employee_id: int,
) -> None:
    stmt = insert(FormerJob).values(
        name=name, job_title=job_title, term=term, date_start=date_start, employee_id=employee_id
    )

    session.execute(stmt)
