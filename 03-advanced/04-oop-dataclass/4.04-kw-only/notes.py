#!/usr/bin/env python3
# https://python3.info/advanced/oop-dataclass/kw-only.html
from dataclasses import dataclass, field, InitVar
from dataclasses import KW_ONLY

# %% Dataclass KWonly
# %%



# %% All Fields
# - Since Python 3.10
# - Mark all fields as keyword-only
# - kw_only=False by default
# %%



# %% Particular Field
# - Since Python 3.10
# - keyword-only
# %%



# %% Following Fields
# - Since Python 3.10
# - from dataclasses import KW_ONLY
# %%


@dataclass
class User:
    fullname: InitVar[str]
    firstname: str | None = None
    lastname: str | None = None
    age: int = field(kw_only=True)

    def __post_init__(self, fullname: str):
        self.firstname, self.lastname = fullname.split()

@dataclass
class Admin(User):
    special_permission: bool = False
    _: KW_ONLY
    has_access_to_erase: bool = False


user = User('Pawel Niedziela', age=50)
admin = Admin('Monia Niedziela', False, age=50, has_access_to_erase=True)
print(user)
print(admin)
