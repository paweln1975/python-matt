@dataclass
class User:
    firstname: str
    lastname: str
    groups: list[Group]

    def __iadd__(self, other):
        self.groups.append(other)
        return self