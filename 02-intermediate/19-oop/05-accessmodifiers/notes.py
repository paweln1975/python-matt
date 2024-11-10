#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/oop/accessmodifiers.html

#%% OOP Access Modifiers
# Attributes and methods are always public
# No protected and private keywords
# Private and protected is only by convention [#pydocprivatevar]_
# name - public attribute
# _name - protected attribute (non-public by convention)
# __name - private attribute (name mangling)
# __name__ - system attribute (dunder)
# name_ - avoid name collision with built-ins



#%% Public Attribute
# name - public attribute



#%% Protected Attribute
# _attrname - protected attribute (non-public by convention)



#%% Private Attribute
# __attrname - private attribute (name mangling)



#%% Name Mangling



#%% Name Collision
# Example colliding names: type_, id_, hash_



#%% System Attributes
# __attrname__ - Current module
# obj.__class__ - Class from which object was instantiated
# obj.__dict__ - Stores instance variables
# obj.__doc__ - Object docstring
# obj.__annotations__ - Object attributes type annotations
# obj.__module__ - Name of a module in which object was defined



#%% Show Attributes
# vars() display obj.__dict__