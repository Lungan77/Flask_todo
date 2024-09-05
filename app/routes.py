from flask import Blueprint, render_template, redirect, url_for, request
from app import db
from app.models import TodoItem
from app.forms import TodoForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = TodoForm()
    if form.validate_on_submit():
        todo = TodoItem(content=form.content.data)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('main.index'))
    todos = TodoItem.query.all()
    return render_template('index.html', form=form, todos=todos)

@main.route('/delete/<int:id>')
def delete(id):
    todo = TodoItem.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/toggle/<int:id>')
def toggle(id):
    todo = TodoItem.query.get_or_404(id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for('main.index'))
