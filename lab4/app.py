from flask import Flask, render_template, request, flash, redirect, url_for
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker, Session

from lab4.models import QuestionModel

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

engine = create_engine(
    "postgresql+psycopg://questions:questions@localhost:5432/question", echo=True, pool_pre_ping=True
)

session_class = sessionmaker(
    autocommit=False, autoflush=True, bind=engine, expire_on_commit=False, class_=Session
)


@app.route("/")
def index():
    return render_template('base.html')


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        question = request.form['question']

        if not question:
            flash('Title is required!')
        else:
            with session_class() as session:
                session.execute(insert(QuestionModel).values(question=question))

            return redirect(url_for('index'))

    return render_template('form.html')
