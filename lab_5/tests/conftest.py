import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.config import settings
from app.db.base import Base
from app.db.models import Teacher, Group, Student, Lesson, Task
from app.main import app


@pytest.fixture(scope="session")
def fastapi_app():
    return app


@pytest.fixture(scope="session")
def config(fastapi_app):
    yield settings


@pytest.fixture()
def client(fastapi_app):
    with TestClient(app=fastapi_app, base_url="http://test") as client:
        yield client


@pytest.fixture()
def engine(config):
    engine = create_engine(config.POSTGRES_CONFIG.URI, echo=True, pool_pre_ping=True)
    yield engine
    engine.dispose()


@pytest.fixture()
def session(engine) -> Session:
    with engine.begin() as conn:
        session = sessionmaker(
            engine,
            class_=Session,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
        )

        Base.metadata.drop_all(conn)
        Base.metadata.create_all(conn)
        with session(bind=conn) as session:
            yield session
            session.flush()
            session.rollback()


@pytest.fixture
def populate_db(session):
    models = [
        Teacher(id=1, first_name='Леонид', last_name='Чайков', second_name='Васильевич'),
        Teacher(id=2, first_name='Иван', last_name='Петров', second_name='Евгеньевич'),

        Group(id=1, name="ПрИ-101"),
        Group(id=2, name="ПрИ-102"),

        Student(id=1, first_name="Василий", last_name="Чайковский", second_name="Ильич", group_id=1),
        Student(id=2, first_name="Василий", last_name="Петров", second_name="Иванович", group_id=1),
        Student(id=3, first_name="Иван", last_name="Иванов", second_name="Иванович", group_id=1),
        Student(id=4, first_name="Виталий", last_name="Капустин", second_name="Евгеньевич", group_id=1),
        Student(id=5, first_name="Евгений", last_name="Деев", second_name="Валерьевич", group_id=1),

        Student(id=6, first_name="Василий", last_name="Васильев", second_name="Ильич", group_id=2),
        Student(id=7, first_name="Василий", last_name="Иванов", second_name="Петрович", group_id=2),
        Student(id=8, first_name="Петр", last_name="Петров", second_name="Петрович", group_id=2),
        Student(id=9, first_name="Арсений", last_name="Капустин", second_name="Евгеньевич", group_id=2),
        Student(id=10, first_name="Маргарита", last_name="Деева", second_name="Петровна", group_id=2),

        Lesson(id=1, theme="Интегралы", tracher_id=1, group_id=1, name="Математика"),
        Lesson(id=2, theme="Программирование на C#", tracher_id=2, group_id=1, name="Программирование"),
        Lesson(id=3, theme="Математическое моделирование", tracher_id=1, group_id=2, name="Математика"),
        Lesson(id=4, theme="ООП", tracher_id=2, group_id=2, name="Программирование"),

        Task(status="UNCHECKED", difficulty_level=2, student_id=1, lesson_id=1),
        Task(status="UNCHECKED", difficulty_level=2, student_id=2, lesson_id=1),
        Task(status="UNCHECKED", difficulty_level=2, student_id=3, lesson_id=1),
        Task(status="UNCHECKED", difficulty_level=2, student_id=4, lesson_id=1),
        Task(status="UNCHECKED", difficulty_level=2, student_id=5, lesson_id=1),

        Task(status="UNCHECKED", difficulty_level=5, student_id=1, lesson_id=2),
        Task(status="UNCHECKED", difficulty_level=5, student_id=2, lesson_id=2),
        Task(status="UNCHECKED", difficulty_level=5, student_id=3, lesson_id=2),
        Task(status="UNCHECKED", difficulty_level=5, student_id=4, lesson_id=2),
        Task(status="UNCHECKED", difficulty_level=5, student_id=5, lesson_id=2),

        Task(status="UNCHECKED", difficulty_level=3, student_id=6, lesson_id=3),
        Task(status="UNCHECKED", difficulty_level=3, student_id=7, lesson_id=3),
        Task(status="UNCHECKED", difficulty_level=3, student_id=8, lesson_id=3),
        Task(status="UNCHECKED", difficulty_level=3, student_id=9, lesson_id=3),
        Task(status="UNCHECKED", difficulty_level=3, student_id=10, lesson_id=3),

        Task(status="UNCHECKED", difficulty_level=4, student_id=6, lesson_id=4),
        Task(status="UNCHECKED", difficulty_level=4, student_id=7, lesson_id=4),
        Task(status="UNCHECKED", difficulty_level=4, student_id=8, lesson_id=4),
        Task(status="UNCHECKED", difficulty_level=4, student_id=9, lesson_id=4),
        Task(status="UNCHECKED", difficulty_level=4, student_id=10, lesson_id=4),
    ]

    session.add_all(models)
    session.commit()
