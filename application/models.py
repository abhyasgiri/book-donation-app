from application import db
from datetime import datetime

class Users(db.Mode):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    books = db.relationship('Books', backref='user')

class Shops(db.Mode):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(30), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    books = db.relationship('Books', backref='shop')

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop_id'), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
