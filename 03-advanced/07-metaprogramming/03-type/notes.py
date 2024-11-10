#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/metaprogramming/type.html

#%% Metaprogramming Type



#%% Recap



#%% Type Behavior
# Type is a class
# Type takes 1 or 3 arguments



#%% Type Working Modes
# type() takes 1 or 3 arguments
# type() has two working modes
# type(obj) returns a class of an object
# type() takes str, tuple, dict
# type(name, bases, attrs) creates a new class



#%% Class Name
# First argument is a str with a name for a new class
# type(name, bases, attrs) creates a new class



#%% Class Bases
# Second argument is a tuple with base classes
# Mind, that one element tuple must have a comma



#%% Class Variables
# Third argument is a dict with class variables
# Mind, that those are class variables
# Class variables share state between all instances



#%% Class Methods
# Third argument (dict) can also contains references to functions
# There is not a big difference, how Python distinguishes between class variables and class methods
# This is the reason, why we collectively call them class attributes
# This functions can take self as an argument, but this is not a requirement
# Function names are not necessary to be the same as in the class
# Dictionary keys decide, how the method will be called later on



#%% All Together



#%% What is a class?



#%% Dynamic Class Creation
# Classes can be created dynamically
# This is a powerful feature of Python
# It allows to create classes on the fly