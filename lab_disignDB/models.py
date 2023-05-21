import datetime

from sqlalchemy import Integer, String, ForeignKey, Date, Boolean
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

convention = {
    "all_column_names": lambda constraint, table: "_".join([column.name for column in constraint.columns.values()]),
    "ix": "ix__%(table_name)s__%(all_column_names)s",
    "uq": "uq__%(table_name)s__%(all_column_names)s",
    "ck": "ck__%(table_name)s__%(constraint_name)s",
    "fk": "fk__%(table_name)s__%(all_column_names)s__" "%(referred_table_name)s",
    "pk": "pk__%(table_name)s",
}

metadata_obj = MetaData(naming_convention=convention)


class Base(DeclarativeBase):
    metadata = metadata_obj


class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    DOB: Mapped[datetime.date] = mapped_column(Date)
    disability: Mapped[bool] = mapped_column(Boolean, default=False)
    child: Mapped[bool] = mapped_column(Boolean, default=False)
    retiree: Mapped[bool] = mapped_column(Boolean, default=False)
    job_title_id: Mapped[int] = mapped_column(ForeignKey('job_title.id'), index=True)


class JobTitle(Base):
    __tablename__ = "job_title"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    job: Mapped[str] = mapped_column(String(20))
    salary: Mapped[int]


class Vacation(Base):
    __tablename__ = "vacation"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    data_from: Mapped[datetime.date] = mapped_column(Date)
    data_to: Mapped[datetime.date] = mapped_column(Date)
    employee_id: Mapped[int] = mapped_column(ForeignKey('employee.id'), index=True)
    categorys_vacation_id: Mapped[int] = mapped_column(ForeignKey('categorys_vacation.id'), index=True)


class FormerJob(Base):
    __tablename__ = "former_job"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    job_title: Mapped[str] = mapped_column(String(20))
    term: Mapped[int]
    date_start: Mapped[datetime.date] = mapped_column(Date)
    employee_id: Mapped[int] = mapped_column(ForeignKey('employee.id'), index=True)


class CategorysVacation(Base):
    __tablename__ = "categorys_vacation"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
