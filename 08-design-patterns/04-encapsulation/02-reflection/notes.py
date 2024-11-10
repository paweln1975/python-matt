#!/usr/bin/env python3

# Reference:
# https://python3.info/design-patterns/encapsulation/reflection.html

#%% Encapsulation Reflection
# setattr(instance, attrname, value) -> None
# delattr(instance, attrname) -> None
# getattr(instance, attrname, default) -> Any
# hasattr(instance, attrname) -> bool



#%% Problem



#%% Set Attribute
# Called when trying to set attribute to a value
# Typing obj.attrname = value
# Will call setattr(obj, attrname, value)
# Which triggers obj.__setattr__(attrname, value)



#%% Delete Attribute
# Called when trying to delete attribute
# Typing del obj.attrname
# Will call delattr(obj, attrname)
# Which triggers mark.__delattr__(name)



#%% Get Attribute If Exists
# Called for every time, when you want to access any attribute
# Before even checking if this attribute exists
# If attribute is not found, then raises AttributeError and calls __getattr__()
# Typing obj.attrname
# Will call getattr(obj, attrname)
# Which triggers obj.__getattribute__(attrname)
# If ok: then return value
# If error: then call obj.__getattr__(attrname)



#%% Get Attribute If Missing
# Called whenever you request an attribute that hasn't already been defined
# It will not execute, when attribute already exist
# Implementing a fallback for missing attributes



#%% Has Attribute
# Check if object has attribute
# There is no __hasattr__() method
# Calling hasattr(obj, attrname)
# Will call __getattribute__() and checks if raises AttributeError
# If no exception, then return True
# If exception, then call __getattr__() and check
# If __getattr__() succeeds then return True
# If __getattr__() fail then return False