import unittest
import time
from flask import url_for
from urllib.request import urlopen

from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Shops

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
        return app

    def setUp(self):
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/abhya/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestTaskCreation(TestBase):
    def test_task_creation(self):
        # Navigate to the Create Task page
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        time.sleep(1)

        # Input the task description into the form field
        self.driver.find_element_by_xpath('//*[@id="shop_name"]').send_keys('Do integration testing')
        self.driver.find_element_by_xpath('//*[@id="location"]').send_keys('Do integration testing')
        
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        # Assert that browser redirects to login page
        assert url_for('home') in self.driver.current_url
        assert Shops.query.filter_by(id=1).first().shop_name == 'Do integration testing'
        assert Shops.query.filter_by(id=1).first().location == 'Do integration testing'

if __name__ == '__main__':
    unittest.main(port=5000)
