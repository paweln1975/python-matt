


class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        firstname = self.firstname
        lastname = self.lastname
        return f'User({firstname=}, {lastname=})'
