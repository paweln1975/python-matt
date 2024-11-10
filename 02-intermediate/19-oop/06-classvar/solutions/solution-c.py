

class User:
    AGE_MIN = 18
    AGE_MAX = 65

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        if not self.AGE_MIN <= self.age <= self.AGE_MAX:
            raise ValueError('Invalid age')
