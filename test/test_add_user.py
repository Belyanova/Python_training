﻿# -*- coding: utf-8 -*-
from model.configurations_user import Configurations_user

def test_user(app):
    old_users = app.user.get_user_list()
    user = Configurations_user("User_name", "name", "Last_name", "Nickname", "Title", "Company", "Address", "999888777",
                          "12345678", "87654321", "e-mail_1", "e-mail_2", "e-mail_3", "1", "April", "1998", "1",
                          "April", "2000", "Address", "Home", "Notes")
    app.user.add_new_user(user)
    new_users=app.user.get_user_list()
    assert len(old_users)+1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=Configurations_user.id_or_max) == sorted(new_users, key=Configurations_user.id_or_max)

