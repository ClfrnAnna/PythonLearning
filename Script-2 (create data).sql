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