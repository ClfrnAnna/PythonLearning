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

INSERT INTO vacation (employee_id, categorys_vacation_id, data_from, data_to) VALUES (2, 2, '2023-03-29', '2024-03-29');
INSERT INTO vacation (employee_id, categorys_vacation_id, data_from, data_to) VALUES (4, 1, '2023-04-30', '2023-05-17');
INSERT INTO vacation (employee_id, categorys_vacation_id, data_from, data_to) VALUES (6, 1, '2023-06-30', '2023-07-15');

INSERT INTO former_job (name, job_title, term, date_start, employee_id) VALUES ('ООО Рога и Копыта', 'Начальник', 3, '2020-04-15', 5);
INSERT INTO former_job (name, job_title, term, date_start, employee_id) VALUES ('ООО Рога и Копыта', 'Начальник', 2, '2018-04-15', 5);
INSERT INTO former_job (name, job_title, term, date_start, employee_id) VALUES ('ООО Конина', 'Рабочий', 2, '2021-04-15', 3);
INSERT INTO former_job (name, job_title, term, date_start, employee_id) VALUES ('ООО Копыта', 'Рабочий', 1, '2022-02-15', 1);
INSERT INTO former_job (name, job_title, term, date_start, employee_id) VALUES ('ООО Конина', 'Рабочий', 2, '2019-07-15', 4);
INSERT INTO former_job (name, job_title, term, date_start, employee_id) VALUES ('ООО КПСС', 'Глава партии', 9, '1917-07-15', 3);