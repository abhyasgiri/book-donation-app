from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    book_title = StringField('Title of the Book', validators = [DataRequired()])
    watchlisted = BooleanField('Do you want this book to be put on your watchlist')
    submit = SubmitField('Add Book')

class ShopForm(FlaskForm):
    shop_name = StringField('Title of the Shop', validators = [DataRequired()])
    location = StringField('Location of the Shop', validators = [DataRequired()])
    submit = SubmitField('Add Shop')