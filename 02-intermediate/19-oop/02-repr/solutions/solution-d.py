
class Accounts:
    def __init__(self, users):
        self.users = users

    def __str__(self):
        return '\n'.join(map(str, self.users))


class User:
    def __init__(self, firstname, lastname, groups=None):
        self.firstname = firstname
        self.lastname = lastname
        self.groups = groups if groups else []

    def __str__(self):
        if self.groups:
            return f'{self.firstname} {self.lastname} member of {self.groups}'
        else:
            return f'{self.firstname} {self.lastname}'


class Group:
    def __init__(self, gid, name):
        self.gid = gid
        self.name = name

    def __repr__(self):
        return f'{self.gid}({self.name})'
