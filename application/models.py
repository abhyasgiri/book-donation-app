from application import db
from datetime import datetime
from hashutils import make_pw_hash

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(100), nullable=False)
    shop_id = db.Column('shop_id', db.Integer, db.ForeignKey('shops.id'), nullable=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable=False, default=1)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    watchlisted = db.Column(db.Boolean, nullable=False, default=0)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False)
    pw_hash = db.Column(db.String(120), nullable=False, server_default='')
    books = db.relationship('Books', backref='user')

    def __init__(self, username, email, password):
        self.username = username
        self.email= email
        self.pw_hash = make_pw_hash(password)

class Shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(30), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    books = db.relationship('Books', backref='shop')


