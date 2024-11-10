
class User:
    def __init__(self, firstname, lastname, groups=None):
        self.firstname = firstname
        self.lastname = lastname
        self.groups = [] if groups is None else groups
