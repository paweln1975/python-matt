#!/usr/bin/env python3
# https://python3.info/advanced/oop-accessor/descriptor.html


# %% Accessor Descriptor
# - Add managed attributes to objects
# - Outsource functionality into specialized classes
# - Descriptors: classmethod, staticmethod, property, functions in general
# - __del__(self) is reserved when object is being deleted by garbage collector (destructor)
# - __set_name() After class creation, Python default metaclass will call it with cls and classname
# %%



# %% Protocol
# - __set_name__(self, owner, name) -> None
# - __get__(self, instance, owner) -> Any
# - __set__(self, instance, value) -> None
# - __delete__(self, instance) -> None
# %%



# %% Problem
# - If one field need to have certain behavior -> Property
# - If all fields need to have certain behavior -> Reflection
# - If selected fields need to have certain behavior -> Descriptor
# %%



# %% Solution
# %%



# %% Inheritance
# %%



# %% Builtin Descriptors
# - Function are Descriptors
# - Classes are Descriptors
# - Methods are Descriptors
# %%



