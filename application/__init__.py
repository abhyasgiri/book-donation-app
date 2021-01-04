from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
app.config["SECRET_KEY"] = getenv("SECRET_KEY")
db = SQLAlchemy(app)

from application import routes