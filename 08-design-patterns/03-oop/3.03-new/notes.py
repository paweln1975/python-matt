#!/usr/bin/env python3
# https://python3.info/design-patterns/oop/new.html


# %% OOP New
# - __new__ - object constructor
# - __init__ - object initializer
# %%



# %% New Method
# - Constructor method
# - cls as it's first parameter
# - when calling __new__() you actually don't have an instance yet, therefore no self exists at that moment
# - It takes the same arguments as __init__()
# %%



# %% Init Method
# - Initializer method
# - for initializing object with initial values
# - self as it's first parameter
# - __init__() is called after __new__() and the instance
# %%



# %% New and Init
# - __new__() is called before __init__()
# - __new__() is responsible for creating the object
# - __init__() is responsible for initializing the object
# - __init__() is called on the object returned by __new__() if it returns an instance of the class
# - if __new__() does not return an instance of the same class, then __init__() will not be called
# %%



# %% Parameters and Arguments
# - __new__ and __init__ should have the same parameters
# - Parameters - variables defined on method definition
# - Arguments - values passed to method on invocation (call)
# %%



# %% Return
# - __new__() is called before __init__()
# - __new__() is responsible for creating the object
# - __init__() is responsible for initializing the object
# - __init__() is called on the object returned by __new__() if it returns an instance of the class
# - if __new__() does not return an instance of the same class, then __init__() will not be called
# %%



