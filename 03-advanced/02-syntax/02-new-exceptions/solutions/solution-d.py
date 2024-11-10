
def login(username, password):
    for user in DATA:
        if user['username'] == username and user['password'] == password:
            return User(username)
    raise User.DoesNotExist
