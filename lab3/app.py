from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from lab3.queries import select_tasks_by_theme, select_tasks_by_difficulty_lvl, select_student_tasks_by_status, \
    select_all_student_tasks, select_group_students_by_teacher, update_student_task_status, \
    get_group_academic_performance_percentage, get_group_name, get_solved_tasks_percentage

app = Flask(__name__)

engine = create_engine(
    "postgresql+psycopg://education:education@localhost:5432/education", echo=True, pool_pre_ping=True
)

session_class = sessionmaker(
    autocommit=False, autoflush=True, bind=engine, expire_on_commit=False, class_=Session
)


@app.route("/")
def index():
    return render_template('base.html')


@app.route('/tasks/get-by-theme/<string:theme>', methods=['GET'])
def get_tasks_by_theme(theme: str):
    with session_class() as session:
        tasks = select_tasks_by_theme(session, theme)

    return render_template('tasks.html', tasks=tasks)


@app.route('/tasks/get-by-difficulty-lvl/<int:difficulty_lvl>', methods=['GET'])
def get_tasks_by_difficulty_lvl(difficulty_lvl: int):
    with session_class() as session:
        tasks = select_tasks_by_difficulty_lvl(session, difficulty_lvl)

    return render_template('tasks.html', tasks=tasks)


@app.route('/tasks/get-by-status', methods=['GET'])
def get_tasks_by_status():
    status = request.args.get("status", "UNCHECKED", str)
    student_id = request.args.get("student_id", 1, int)

    with session_class() as session:
        tasks = select_student_tasks_by_status(session, status, student_id)

    return render_template('tasks.html', tasks=tasks)


@app.route('/tasks/get-by-student-id', methods=['GET'])
def get_tasks_by_student_id():
    student_id = request.args.get("student_id", 1, int)

    with session_class() as session:
        tasks = select_all_student_tasks(session, student_id)

    return render_template('tasks.html', tasks=tasks)


@app.route('/group/<int:group_id>/students', methods=['GET'])
def get_group_students(group_id: int):
    teacher_id = request.args.get("teacher_id", 1, int)
    lesson_id = request.args.get("lesson_id", 1, int)

    with session_class() as session:
        students = select_group_students_by_teacher(session, group_id, teacher_id, lesson_id)

    return render_template('students.html', students=students)


@app.route('/students/<int:student_id>/tasks/<int:task_id>', methods=["GET", "POST"])
def update_task_status(student_id: int, task_id: int):
    if request.method == 'POST':
        status = request.form['status']

        with session_class() as session:
            update_student_task_status(session, task_id, student_id, status)

        return redirect(url_for('index'))

    return render_template('task_update.html')


@app.route('/group/<int:group_id>/receive-academic-performance', methods=['GET'])
def get_group_academic_performance(group_id: int):

    with session_class() as session:
        group_name = get_group_name(session, group_id)
        percentage = get_group_academic_performance_percentage(session, group_id)

    return render_template('group_performance_stat.html', group_name=group_name, percentage=percentage)


@app.route('/tasks/receive-academic-performance', methods=['GET'])
def get_tasks_performance():
    with session_class() as session:
        percentage = get_solved_tasks_percentage(session)

    return render_template('task_performance_stat.html', percentage=percentage)
