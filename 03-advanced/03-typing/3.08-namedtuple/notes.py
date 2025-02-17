#!/usr/bin/env python3
# https://python3.info/advanced/typing/namedtuple.html
from typing import NamedTuple


# %% Typing NamedTuple
# - NamedTuple is a class that allows you to create a tuple with named fields.
# - NamedTuple is immutable.
# %%

class User(NamedTuple):
    firstname: str
    lastname: str
    age: int | None = None


user = User(firstname="John", lastname="Doe")
print(user.firstname)
print(user.lastname)
print(user.age)

# %% Problem
# %%



# %% Solution
# %%



# %% Default
# %%



# %% Field Access
# - You can access fields by name or index.
# %%



# %% Is Instance
# - NamedTuple is a subclass of tuple
# %%



# %% Further Reading
# - Example: https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
# - More information in Type Annotations
# - More information in CI/CD Type Checking
# %%



