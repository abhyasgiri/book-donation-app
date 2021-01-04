from application import db
from application.models import Users

db.drop_all()
db.create_all()

first_user = Users(username= "Fred", email= "fred@bookdonation.com", password= "secret")
second_user = Users(username= "Samantha", email= "samantha@bookdonation.com", password= "secret")
db.session.add(first_user)
db.session.add(second_user)
db.session.commit()