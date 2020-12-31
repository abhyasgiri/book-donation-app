from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class BookForm(FlaskForm):
    book_title = StringField('Title of the Book', validators = [DataRequired()])
    watchlisted = BooleanField('Do you want this book to be put on your watchlist')
    submit = SubmitField('Add Book')

class ShopForm(FlaskForm):
    shop_name = StringField('Title of the Shop', validators = [DataRequired()])
    location = StringField('Location of the Shop', validators = [DataRequired()])
    submit = SubmitField('Add Shop')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')