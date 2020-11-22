﻿# -*- coding: utf-8 -*-
from model.configurations_user import Configurations_user
from random import randrange

def test_delete_first_group(app):
    user = Configurations_user("User_name", "name", "Last_name", "Nickname", "Title", "Company", "Address", "999888777",
                               "12345678", "87654321", "e-mail_1", "e-mail_2", "e-mail_3", "1", "April", "1998", "1",
                               "April", "2000", "Address", "Home", "Notes")
    if app.user.count() == 0:
        app.user.add_new_user(user)
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    app.user.delete_user_by_index(index)
    assert len(old_users) - 1 == app.user.count()
    new_users = app.user.get_user_list()
    old_users[index:index+1] = []
    assert old_users == new_users