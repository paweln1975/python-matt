#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/type-logic/bool.html

#%% Logic Bool
# True - Positive value
# False - Negative value
# Builtin function bool() converts argument to bool



#%% Syntax
# First letter capitalized, other are lower cased

x = True

#%% Type Conversion
# Builtin function bool() converts argument to bool

bool(1)

#%% Negative values
# int() or 0 - zero integer
# float() or 0.0 - zero float
# bool() or False - false bool
# str() or '' - empty str
# tuple() or () - empty tuple
# list() or [] - empty list
# set() or set() - empty set
# dict() or {} - empty dict

# empty gives False

print(bool.mro())

#%% Comparison
# x < y - Less than
# x <= y - Less or equal
# x > y - Greater than
# x >= y - Greater or equal
# == - Equals
# != - Not Equals



#%% Negation
# not ... - negation



#%% Conjunction
# ... and ... - conjunction



#%% Disjunction
# ... or ... - disjunction



#%% Boolean Algebra
# and has higher precedence
# or has lower precedence
# use round brackets ( and ) to make code more readable

x = (True and False) or True
print(x)
