class User:
    __slots__ = ('firstname', 'lastname')

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname