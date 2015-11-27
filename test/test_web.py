# coding=utf-8
from selenium import webdriver

class TestWeb(object):
    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:5000')

    def teardown_class(self):
        self.driver.close()

    def test_A(self):
        assert 1 == 1

    def test_B(self):
        assert 1 == 2