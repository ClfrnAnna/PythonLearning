import datetime

from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session

from lab_disignDB.commands import insert_vacation_category, insert_job_title, insert_employee, insert_vacation, \
    insert_former_job
from lab_disignDB.models import CategorysVacation

app = Flask(__name__)

engine = create_engine(
    "postgresql+psycopg://education:education@localhost:5432/department", echo=True, pool_pre_ping=True
)

session_class = sessionmaker(
    autocommit=False, autoflush=True, bind=engine, expire_on_commit=False, class_=Session
)


@app.route("/")
def index():
    return render_template('base.html')


@app.route('/vacation-categories', methods=['GET', 'POST'])
def create_vacation_category():
    if request.method == 'POST':
        category_name = request.form['category_name']

        with session_class() as session:
            insert_vacation_category(session, category_name)

        return redirect(url_for('index'))

    return render_template('vacation_categories.html')


@app.route('/job-titles', methods=['GET', 'POST'])
def create_job_title():
    if request.method == 'POST':
        job = request.form['job']

        try:
            salary = int(request.form['salary'])
        except ValueError:
            flash("salary field must be integer")
            return render_template('job_title.html')

        with session_class() as session:
            insert_job_title(session, job, salary)

        return redirect(url_for('index'))

    return render_template('job_title.html')


@app.route('/job-titles/<int:job_title_id>/employees', methods=['GET', 'POST'])
def create_employee(job_title_id: int):
    if request.method == 'POST':
        name = request.form['name']
        date = datetime.datetime.strptime(request.form['dob'], "%Y-%m-%d").date()
        child = bool(int(request.form["child"]))
        disability = bool(int(request.form["disability"]))
        retiree = bool(int(request.form["retiree"]))

        with session_class() as session:
            insert_employee(session, name, date, child, disability, retiree, job_title_id)

        return redirect(url_for('index'))

    return render_template('employee.html')


@app.route('/employees/<int:employee_id>/vacations', methods=['GET', 'POST'])
def create_vacation(employee_id: int):
    if request.method == 'POST':
        data_from = datetime.datetime.strptime(request.form['data_from'], "%Y-%m-%d").date()
        data_to = datetime.datetime.strptime(request.form['data_to'], "%Y-%m-%d").date()
        categorys_vacation_id = int(request.form['categorys_vacation_id'])

        with session_class() as session:
            insert_vacation(session, data_from, data_to, employee_id, categorys_vacation_id)

        return redirect(url_for('index'))

    with session_class() as session:
        category_vacations = session.scalars(select(CategorysVacation)).all()

    return render_template('vacation.html', category_vacations=category_vacations)


@app.route('/employees/<int:employee_id>/former-jobs', methods=['GET', 'POST'])
def create_former_job(employee_id: int):
    if request.method == 'POST':
        name = request.form['name']
        job_title = request.form['job_title']

        try:
            term = int(request.form['term'])
        except ValueError:
            flash("salary field must be integer")
            return render_template('job_title.html')

        date_start = datetime.datetime.strptime(request.form['data_start'], "%Y-%m-%d").date()

        with session_class() as session:
            insert_former_job(session, name, job_title, term, date_start, employee_id)

        return redirect(url_for('index'))

    return render_template('former_job.html')
