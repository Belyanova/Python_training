﻿from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.user import UserHelper
from fixture.group import GroupHelper
import unittest

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/index.php")

    def destroy(self):
        self.wd.quit()