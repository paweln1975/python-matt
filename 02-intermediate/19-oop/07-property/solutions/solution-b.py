
class User:
    def __init__(self, firstname, lastname, birthdate):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate

    @property
    def age(self):
        today = date.today()
        days = (today - self.birthdate).days
        return int(days / YEAR)
