class Group:
    gid: int
    name: str

    def __init__(self, gid: int, name: str) -> None:
        self.gid = gid
        self.name = name

    def __eq__(self, other):
        return (self.gid == other.gid) \
           and (self.name == other.name)


class User:
    firstname: str
    lastname: str
    groups: list[Group]

    def __init__(self, firstname: str, lastname: str, groups: list) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.groups = groups

    def __contains__(self, flight):
        return flight in self.groups