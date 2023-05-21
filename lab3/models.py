from typing import Optional

from sqlalchemy import Integer, String, ForeignKey, SmallInteger

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


class Student(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    second_name: Mapped[Optional[str]] = mapped_column(String(255))
    group_id: Mapped[int] = mapped_column(ForeignKey("group.id"), index=True)


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    status: Mapped[str] = mapped_column(String(40), default="UNCHECKED")
    difficulty_level: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    student_id: Mapped[int] = mapped_column(ForeignKey("student.id"), index=True)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lesson.id"), index=True)


class Group(Base):
    __tablename__ = "group"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(40))


class Teacher(Base):
    __tablename__ = "teacher"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    second_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)


class Lesson(Base):
    __tablename__ = "lesson"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    theme: Mapped[str] = mapped_column(String(50))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teacher.id"), index=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("group.id"), index=True)
    name: Mapped[str] = mapped_column(String(255))
