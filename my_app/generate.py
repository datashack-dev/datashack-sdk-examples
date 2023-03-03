from my_app.models.users import Users


if __name__ == '__main__':
    Users.insert({'id': '111', 'age': 43, 'name': "yosi"})
    Users.insert({'id': '222', 'age': 30, 'name': "avi"})
    Users.insert({'id': '333', 'age': 38, 'name': "shlomi"})
