from flask import Blueprint, render_template, request, current_app, redirect, flash
from flask_login import current_user, login_required

from todo_app.extensions import db
from todo_app.models import Todo

routes = Blueprint('main', __name__)


@routes.route('/')
def home():
    todos = None
    if current_user.is_authenticated:
        todos = current_user.todos
    return render_template('main/index.html', todos=todos or list())


@routes.route('/add_todo')
def add_todo():
    todo_text = request.args.get('todo')
    todos = None

    if current_user.is_authenticated:
        todo = Todo(todo=todo_text, user_id=current_user.id)
        db.session.add(todo)
        db.session.commit()
        todos = current_user.todos

    return render_template('main/index.html', todos=todos or list())


@routes.route('/remove_todo')
def remove_todo():
    todos = None

    if current_user.is_authenticated:
        todo_id = request.args.get('todo_id', '')
        todo = Todo.query.filter_by(id=todo_id).first()
        if todo:
            db.session.delete(todo)
            db.session.commit()
        todos = current_user.todos

    return render_template('main/index.html', todos=todos or list())
