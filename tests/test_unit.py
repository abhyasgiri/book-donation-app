import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import ___

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:Clpm425N6xjC0Nmz@35.242.128.108/book_donation_db",
            SECRET_KEY="liabafeuhdanksllnksad",
            DEBUG=True
        )
        return app

    def setUp(self):
        db.create_all()
        test_shop = Shops(shop_name= "     ", location=  "    ")
        db.session.add(test_shop)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_createshop_get(self):
        response = self.client.get(url_for('createshop', shop_id=1))
        self.assertEqual(response.status_code, 200)

    def test_update_shop_get(self):
        response = self.client.get(url_for('update_shop', id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete_shop', id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)

class TestRead(TestBase):
    def test_read_shop(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"     ")     #insert in what we put up in setup Shops( ..... )

class TestCreate(TestBase):
    def test_create_shop(self):
        response = self.client.post(
            url_for("createshop"), 
            data = dict(shop_name = " ", location = " "), 
            follow_redirects=True
        )
        self.assertIn(b"       ", response.data)
    
class TestUpdate(TestBase):
    def test_update_shop(self):
        response = self.client.post(
            url_for("update_shop", id=1), 
            data = dict(shop_name = " ", location = " "), 
            follow_redirects=True
        )
        self.assertIn(b"       ", response.data)

class TestDelete(TestBase):
    def test_delete_shop(self):
        response = self.client.get(
            url_for("delete_shop", id=1),
            follow_redirects=True
        )
        self.assertIn(b"       ", response.data)