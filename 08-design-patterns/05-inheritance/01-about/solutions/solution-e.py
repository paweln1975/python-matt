
class Account:
    pass


class User(Account):
    pass


class Admin(Account):
    pass


class MyAccount:
    type: Account

    def __init__(self, type: Account = Account):
        self.type = type()
