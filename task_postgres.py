# link: https://editor.ponyorm.com/user/Clfrn42/Department/designer

import psycopg
from psycopg import Cursor
from psycopg.rows import dict_row


def create_tables(cursor) -> None:
    cursor.execute(
        """
        CREATE TABLE "categorys_vacation" (
          "id" SERIAL PRIMARY KEY,
          "name" VARCHAR(20) NOT NULL
        );

        CREATE TABLE "job_title" (
          "id" SERIAL PRIMARY KEY,
          "job" VARCHAR(20) NOT NULL,
          "salary" INTEGER
        );

        CREATE TABLE "employee" (
          "id" SERIAL PRIMARY KEY,
          "name" VARCHAR(50) NOT NULL,
          "dob" DATE,
          "disability" BOOLEAN,
          "child" BOOLEAN,
          "retiree" BOOLEAN,
          "job_title_id" INTEGER NOT NULL
        );

        CREATE INDEX "idx_employee__job_title_id" ON "employee" ("job_title_id");

        ALTER TABLE "employee" ADD CONSTRAINT "fk_employee__job_title_id" FOREIGN KEY ("job_title_id") REFERENCES "job_title" ("id") ON DELETE CASCADE;

        CREATE TABLE "former_job" (
          "id" SERIAL PRIMARY KEY,
          "name" VARCHAR(50) NOT NULL,
          "job_title" VARCHAR(20) NOT NULL,
          "term" INTEGER,
          "date_start" DATE,
          "employee_id" INTEGER NOT NULL
        );

        CREATE INDEX "idx_former_job__employee_id" ON "former_job" ("employee_id");

        ALTER TABLE "former_job" ADD CONSTRAINT "fk_former_job__employee_id" FOREIGN KEY ("employee_id") REFERENCES "employee" ("id") ON DELETE CASCADE;

        CREATE TABLE "vacation" (
          "id" SERIAL PRIMARY KEY,
          "data_from" DATE,
          "data_to" DATE,
          "employee_id" INTEGER NOT NULL,
          "categorys_vacation_id" INTEGER NOT NULL
        );

        CREATE INDEX "idx_vacation__categorys_vacation_id" ON "vacation" ("categorys_vacation_id");

        CREATE INDEX "idx_vacation__employee_id" ON "vacation" ("employee_id");

        ALTER TABLE "vacation" ADD CONSTRAINT "fk_vacation__categorys_vacation_id" FOREIGN KEY ("categorys_vacation_id") REFERENCES "categorys_vacation" ("id") ON DELETE CASCADE;

        ALTER TABLE "vacation" ADD CONSTRAINT "fk_vacation__employee_id" FOREIGN KEY ("employee_id") REFERENCES "employee" ("id") ON DELETE CASCADE
        """
    )


def insert_values(cursor: Cursor) -> None:
    cursor.execute(
        """
        INSERT INTO categorys_vacation (name) VALUES ('Очередной отпуск');
        INSERT INTO categorys_vacation (name) VALUES ('Декрет');
        
        INSERT INTO job_title (job, salary) VALUES ('Начальник', 50000);
        INSERT INTO job_title (job, salary) VALUES ('Рабочий', 30000);
        
        INSERT INTO employee (name, dob, disability, child, retiree, job_title_id) VALUES ('Пупкин Петр Евгеньевич', '02-11-1980', false, true, false, 1);
        INSERT INTO employee (name, dob, disability, child, retiree, job_title_id) VALUES ('Алешкин Петр Николаевич', '02-12-1990', false, false, false, 2);
        INSERT INTO employee (name, dob, disability, child, retiree, job_title_id) VALUES ('Пупкина Алена Николевчна', '02-12-1981', false, true, false, 2);
        INSERT INTO employee (name, dob, disability, child, retiree, job_title_id) VALUES ('Алешкина Вера Валерьевна', '02-12-1994', false, false, false, 2);
        INSERT INTO employee (name, dob, disability, child, retiree, job_title_id) VALUES ('Ульянов Владимир Ильич', '02-12-1917', false, false, true, 1);
        INSERT INTO employee (name, dob, disability, child, retiree, job_title_id) VALUES ('Попов Алеша Попович', '02-12-1994', false, false, true, 2);
        
        INSERT INTO vacation (employee_id, categorys_vacation_id, data_from, data_to) VALUES (3, 2, '2023-03-29', '2024-03-29');
        INSERT INTO vacation (employee_id, categorys_vacation_id, data_from, data_to) VALUES (2, 1, '2023-04-30', '2023-05-17');
        INSERT INTO vacation (employee_id, categorys_vacation_id, data_from, data_to) VALUES (5, 1, '2023-05-05', '2023-05-20');
        INSERT INTO vacation (employee_id, categorys_vacation_id, data_from, data_to) VALUES (1, 1, '2023-06-30', '2023-07-15');
        
        INSERT INTO former_job (name, job_title, term, date_start, employee_id) VALUES ('ООО Рога и Копыта', 'Начальник', 3, '2020-04-15', 1);
        INSERT INTO former_job (name, job_title, term, date_start, employee_id) VALUES ('ООО Рога и Копыта', 'Начальник', 2, '2018-04-15', 1);
        INSERT INTO former_job (name, job_title, term, date_start, employee_id) VALUES ('ООО Конина', 'Рабочий', 2, '2021-04-15', 2);
        INSERT INTO former_job (name, job_title, term, date_start, employee_id) VALUES ('ООО Копыта', 'Рабочий', 1, '2022-02-15', 3);
        INSERT INTO former_job (name, job_title, term, date_start, employee_id) VALUES ('ООО Конина', 'Рабочий', 2, '2019-07-15', 4);
        INSERT INTO former_job (name, job_title, term, date_start, employee_id) VALUES ('ООО КПСС', 'Глава партии', 9, '1917-07-15', 5);
        """
    )


def select_employee_in_vacation(cursor: Cursor) -> None:
    cursor.execute(
        """
        SELECT em.name, jt.job, jt.salary FROM employee AS em
        JOIN job_title jt ON em.job_title_id = jt.id
        JOIN vacation vac ON em.id = vac.employee_id
        WHERE (em.child = true OR em.retiree = true)
        AND CURRENT_DATE BETWEEN vac.date_from and date_to;
        """
    )
    values = cursor.fetchall()

    for record in values:
        print(record)


def select_employee_position(cursor: Cursor) -> None:
    cursor.execute(
        """
        SELECT em.id, em.name, jt.job FROM employee AS em
        JOIN job_title jt ON em.job_title_id = jt.id;
        """
    )

    values = cursor.fetchall()

    for record in values:
        print(record)


def select_employees_former_jobs(cursor: Cursor) -> None:
    cursor.execute(
        """
        SELECT em.id, em.name, fj.* FROM employee as em
        LEFT JOIN former_job fj on em.id = fj.employee_id;
        """
    )

    for record in cursor.fetchall():
        print(record)


def search_employee(cursor: Cursor, name: str) -> None:
    cursor.execute(
        """
        SELECT * FROM employee
        WHERE name = %(name)s;
        """,
        params={"name": name}
    )

    print(cursor.fetchone())


with psycopg.connect("postgresql://anns_test_db:Anna421198@localhost:5432/DepDB", row_factory=dict_row) as conn:
    with conn.cursor() as cur:
        # create_tables(cur)
        # insert_values(cur)
        select_employee_in_vacation(cur)
        select_employee_position(cur)
        select_employees_former_jobs(cur)
        search_employee(cur, input())
