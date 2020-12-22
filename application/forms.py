from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    description = StringField('Title of the Book', validators = [DataRequired()])
    submit = SubmitField('Add Book')