﻿# -*- coding: utf-8 -*-
from model.configurations_login import Configurations_login
from model.configurations_user import Configurations_user

def test_user(app):
    user = Configurations_user("User_name", "name", "Last_name", "Nickname", "Title", "Company", "Address", "999888777",
                          "12345678", "87654321", "e-mail_1", "e-mail_2", "e-mail_3", "1", "April", "1998", "1",
                          "April", "2000", "Address", "Home", "Notes")
    app.user.add_new_user(user)
