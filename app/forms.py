from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Add Todo')
