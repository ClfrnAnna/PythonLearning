import os

import psycopg
from psycopg.rows import dict_row


def create_tables(cursor: psycopg.Cursor) -> None:
    cursor.execute(
        """
        CREATE TABLE "group" (
          "id" SERIAL PRIMARY KEY,
          "name" VARCHAR(50) NOT NULL
        );
        
        CREATE TABLE "student" (
          "id" SERIAL PRIMARY KEY,
          "first_name" VARCHAR(255) NOT NULL,
          "last_name" VARCHAR(255) NOT NULL,
          "second_name" VARCHAR(255) NOT NULL,
          "group_id" INTEGER NOT NULL
        );
        
        CREATE INDEX "idx_student__group_id" ON "student" ("group_id");
        
        ALTER TABLE "student" ADD CONSTRAINT "fk_student__group_id" FOREIGN KEY ("group_id") REFERENCES "group" ("id") ON DELETE CASCADE;
        
        CREATE TABLE "teacher" (
          "id" SERIAL PRIMARY KEY,
          "first_name" VARCHAR(255) NOT NULL,
          "last_name" VARCHAR(255) NOT NULL,
          "second_name" VARCHAR(255) NOT NULL
        );
        
        CREATE TABLE "lesson" (
          "id" SERIAL PRIMARY KEY,
          "theme" VARCHAR(50) NOT NULL,
          "teacher_id" INTEGER NOT NULL,
          "group_id" INTEGER NOT NULL,
          "name" VARCHAR(50) NOT NULL
        );
        
        CREATE INDEX "idx_lesson__group_id" ON "lesson" ("group_id");
        
        CREATE INDEX "idx_lesson__teacher_id" ON "lesson" ("teacher_id");
        
        ALTER TABLE "lesson" ADD CONSTRAINT "fk_lesson__group_id" FOREIGN KEY ("group_id") REFERENCES "group" ("id") ON DELETE CASCADE;
        
        ALTER TABLE "lesson" ADD CONSTRAINT "fk_lesson__teacher_id" FOREIGN KEY ("teacher_id") REFERENCES "teacher" ("id") ON DELETE CASCADE;
        
        CREATE TABLE "task" (
          "id" SERIAL PRIMARY KEY,
          "status" VARCHAR(40) NOT NULL DEFAULT UNCHECKED,
          "difficalty_level" SMALLINT NOT NULL,
          "student_id" INTEGER NOT NULL,
          "lesson_id" INTEGER NOT NULL
        );
        
        CREATE INDEX "idx_task__lesson_id" ON "task" ("lesson_id");
        
        CREATE INDEX "idx_task__student_id" ON "task" ("student_id");
        
        ALTER TABLE "task" ADD CONSTRAINT "fk_task__lesson_id" FOREIGN KEY ("lesson_id") REFERENCES "lesson" ("id") ON DELETE CASCADE;
        
        ALTER TABLE "task" ADD CONSTRAINT "fk_task__student_id" FOREIGN KEY ("student_id") REFERENCES "student" ("id") ON DELETE CASCADE
        """
    )


def insert_values(cursor: psycopg.Cursor) -> None:
    cursor.execute(
        """
        INSERT INTO teacher (id, first_name, last_name, second_name) VALUES (1, 'Леонид', 'Чайков', 'Васильевич');
        INSERT INTO teacher (id, first_name, last_name, second_name) VALUES (2, 'Иван', 'Петров', 'Евгеньевич');
        
        
        INSERT INTO "group" (id, "name") VALUES (1, 'ПрИ-101');
        INSERT INTO "group" (id, "name") VALUES (2, 'ПрИ-102');
        
        
        INSERT INTO student (id, first_name, last_name, second_name, group_id) VALUES (1, 'Василий', 'Чайковский', 'Ильич', 1);
        INSERT INTO student (id, first_name, last_name, second_name, group_id) VALUES (2, 'Василий', 'Петров', 'Иванович', 1);
        INSERT INTO student (id, first_name, last_name, second_name, group_id) VALUES (3, 'Иван', 'Иванов', 'Иванович', 1);
        INSERT INTO student (id, first_name, last_name, second_name, group_id) VALUES (4, 'Виталий', 'Капустин', 'Евгеньевич', 1);
        INSERT INTO student (id, first_name, last_name, second_name, group_id) VALUES (5, 'Евгений', 'Деев', 'Валерьевич', 1);
        
        INSERT INTO student (id, first_name, last_name, second_name, group_id) VALUES (6, 'Василий', 'Васильев', 'Ильич', 2);
        INSERT INTO student (id, first_name, last_name, second_name, group_id) VALUES (7, 'Василий', 'Иванов', 'Петрович', 2);
        INSERT INTO student (id, first_name, last_name, second_name, group_id) VALUES (8, 'Петр', 'Петров', 'Петрович', 2);
        INSERT INTO student (id, first_name, last_name, second_name, group_id) VALUES (9, 'Арсений', 'Капустин', 'Евгеньевич', 2);
        INSERT INTO student (id, first_name, last_name, second_name, group_id) VALUES (10, 'Маргарита', 'Деева', 'Петровна', 2);
        
        
        INSERT INTO lesson (id, theme, teacher_id, group_id, "name") VALUES (1, 'Интегралы', 1, 1, 'Математика');
        INSERT INTO lesson (id, theme, teacher_id, group_id, "name") VALUES (2, 'Программирование на C#', 2, 1, 'Программирование');
        INSERT INTO lesson (id, theme, teacher_id, group_id, "name") VALUES (3, 'Математическое моделирование', 1, 2, 'Математика');
        INSERT INTO lesson (id, theme, teacher_id, group_id, "name") VALUES (4, 'ООП', 2, 2, 'Программирование');
        
        
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 2, 1, 1);
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 2, 2, 1);
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 2, 3, 1);
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 2, 4, 1);
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 2, 5, 1);
        
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 5, 1, 2);
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 5, 2, 2);
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 5, 3, 2);
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 5, 4, 2);
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 5, 5, 2);
        
        
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 3, 6, 3);
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 3, 7, 3);
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 3, 8, 3);
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 3, 9, 3);
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 3, 10, 3);
        
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 4, 6, 4);
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 4, 7, 4);
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 4, 8, 4);
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 4, 9, 4);
        INSERT INTO task (status, difficulty_level, student_id, lesson_id) VALUES ('UNCHECKED', 4, 10, 4);
        """
    )


def select_tasks_by_theme(cursor: psycopg.Cursor, theme: str) -> None:
    cursor.execute(
        """ 
        SELECT t.* FROM task t
        JOIN lesson l on l.id = t.lesson_id
        WHERE l.theme = %(theme)s;
        """,
        params={"theme": theme}
    )

    for task in cursor.fetchall():
        print(task)


def select_tasks_by_difficulty_lvl(cursor: psycopg.Cursor, lvl: int) -> None:
    cursor.execute(
        """ 
        SELECT * FROM task t
        WHERE t.difficulty_level = %(difficulty_level)s;
        """,
        params={"difficulty_level": lvl}
    )

    for task in cursor.fetchall():
        print(task)


def select_student_tasks_by_status(cursor: psycopg.Cursor, status: str, student_id: int) -> None:
    cursor.execute(
        """ 
        SELECT t.* FROM task t
        JOIN student s on s.id = t.student_id
        WHERE s.id = %(id)s
        AND t.status = %(status)s;
        """,
        params={
            "id": student_id,
            "status": status,
        }
    )

    for task in cursor.fetchall():
        print(task)


def select_all_student_tasks(cursor: psycopg.Cursor, student_id: int) -> None:
    cursor.execute(
        """ 
        SELECT t.* FROM task t
        JOIN student s on s.id = t.student_id
        WHERE s.id = %(id)s;
        """,
        params={
            "id": student_id,
        }
    )

    for task in cursor.fetchall():
        print(task)


def select_group_students_by_teacher(cursor: psycopg.Cursor, group_id: int, teacher_id: int, lesson_id: int) -> None:
    cursor.execute(
        """ 
        SELECT s.* FROM student s
        JOIN "group" g on g.id = s.group_id
        JOIN lesson l on g.id = l.group_id
        WHERE g.id = %(group_id)s
          AND l.teacher_id = %(teacher_id)s
          AND l.id = %(lesson_id)s;
        """,
        params={
            "group_id": group_id,
            "teacher_id": teacher_id,
            "lesson_id": lesson_id,
        }
    )

    for student in cursor.fetchall():
        print(student)


def update_student_task_status(cursor: psycopg.Cursor, task_id: int, student_id: int, status: str) -> None:
    cursor.execute(
        """ 
        UPDATE task SET status = %(status)s WHERE student_id = %(student_id)s AND id = %(task_id)s;
        """,
        params={
            "task_id": task_id,
            "student_id": student_id,
            "status": status,
        }
    )


def get_solved_tasks_percentage(cursor: psycopg.Cursor) -> None:
    cursor.execute(
        """
        SELECT (sum(CASE WHEN status = 'SOLVED' THEN 1 ELSE 0 END)/CAST(count(*) AS FLOAT))*100 percentage FROM task;
        """
    )

    print(cursor.fetchone())


def get_group_academic_performance_percentage(cursor: psycopg.Cursor, group_id) -> None:
    cursor.execute(
        """
        SELECT (sum(CASE WHEN status = 'SOLVED' THEN 1 ELSE 0 END)/CAST(count(*) AS FLOAT))*100 percentage FROM task
        JOIN student s on s.id = task.student_id
            WHERE s.group_id = %(group_id)s;
        """,
        params={
            "group_id": group_id,
        }
    )

    print(cursor.fetchone())


def create_tasks_files(cursor: psycopg.Cursor) -> None:
    cursor.execute(
        """
        SELECT id FROM task
        """
    )

    if not os.path.exists("./classwork"):
        os.mkdir("./classwork", mode=0o777)

    for task in cursor.fetchall():
        open(f"./classwork/task_{task['id']}.py", "w").close()


with psycopg.connect("postgresql://education:education@localhost:5432/education", row_factory=dict_row) as conn:
    with conn.cursor() as cur:
        select_tasks_by_theme(cur, "Интегралы")
        print("\n")

        select_tasks_by_difficulty_lvl(cur, 3)
        print("\n")

        select_student_tasks_by_status(cur, "UNCHECKED", 5)
        print("\n")
        select_student_tasks_by_status(cur, "SOLVED", 5)
        print("\n")

        select_all_student_tasks(cur, 1)
        print("\n")

        select_group_students_by_teacher(cur, 1, 1, 1)
        print("\n")

        update_student_task_status(cur, 5, 5, "SOLVED")

        get_solved_tasks_percentage(cur)

        get_group_academic_performance_percentage(cur, 1)

        create_tasks_files(cur)
