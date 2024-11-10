#!/usr/bin/env python3

# Reference:
# https://python3.info/oop/python/new-style-classes.html

#%% New and Old Style Class
# Old Style classes - Not existing in Python 3
# In Python 3 class will always produce new style class
# The major motivation for introducing new-style classes is to provide a unified object model with a full meta-model
# https://docs.python.org/dev/tutorial/classes.html



#%% Old Style classes
# Not existing in Python 3
# Don't inherit from object
# In Python 3, there are no old-style classes, and this code will produce new style class



#%% New Style Class
# Introduced in Python 2.2
# In Python 3 this is the only way
# Inherit from object or from another new style class
# Ability to subclass most built-in types
# super() added
# MRO changed
# descriptors added
# new style class objects cannot be raised unless derived from Exception
# __slots__ added



#%% Definition
# Old style classes are **only** in Python 2
# New style classes works in Python 2 (when inherit from object)
# In Python 3 all classes always inherit from object, hence they are new style classes