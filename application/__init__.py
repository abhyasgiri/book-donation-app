from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Clpm425N6xjC0Nmz@35.242.128.108/book_donation_db"
app.config["SECRET_KEY"] = "liabafeuhdanksllnksad"
db = SQLAlchemy(app)

from application import routes 