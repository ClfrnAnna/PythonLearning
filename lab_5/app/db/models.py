from typing import Optional

from sqlalchemy import Integer, String, ForeignKey, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


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
