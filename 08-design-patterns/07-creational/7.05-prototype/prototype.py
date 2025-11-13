import copy
from typing import Literal
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class User:
    firstname: str
    lastname: str
    username: str
    password: str
    email: str
    lastlogin: datetime | None
    role: Literal["user", "admin", "staff"]
    groups: list[str] = field(default_factory=list)

    def clone(self, **kwargs) -> User:
        values = vars(self) | kwargs
        values |= {'groups': [g for g in self.groups]}
        cls = self.__class__
        return cls(**values)

    def copy(self) -> User:
        c = copy.deepcopy(self)
        return c

@dataclass
class Admin(User):
    pass

mark = Admin(firstname="Mark", lastname="Smith", username="marks", role="admin",
             password="", email="mark@nasa.gov", lastlogin=datetime.now(),
             groups=["admin", "user"])

melissa = mark.clone(firstname = "Melissa", lastname="Melissa", username="melissa", email="melissa@nasa.gov")

melissa_copy = melissa.copy()

mark.groups.append("staff")
print(mark)
print(melissa)
print(melissa_copy)

