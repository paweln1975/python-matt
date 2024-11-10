#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/unpack/assignment.html

#%% Unpack Assignment
# a = 1 - Assignment
# a, b = 1, 2 - Unpacking assignment
# a = b = 1 - Chained assignment
# _ is regular variable name, not a special Python syntax
# _ by convention is used for data we don't want to access in future



#%% Assignment
# Scalar Assignment
# identifier = object
# a = 1
# a = 1, 2



#%% Unpacking Assignment
# iterable[identifier] = iterable[object]
# a, b = 1, 2
# a, b, c = 1, 2, 3
# Sequence -> tuple, list
# Iterable -> tuple, list, set, frozenset, dict, ...
# Length at right and left side must be the same



#%% Chained Assignment
# identifier1 = identifier2 = object
# a = b = 1
# a = b = c = 1



#%% Chained Unpacking Assignment
# iterable[identifier] = iterable[identifier] = iterable[object]



#%% Brackets



#%% Swap
# Swap two variables



#%% Unpacking



#%% Nested



#%% Skipping Values
# _ is regular variable name, not a special Python syntax
# _ by convention is used for data we don't want to access in future



#%% Copy Deep vs Reference



#%% Recap
# Four types of assignments: Scalar, Unpacking, Chained, Chained Unpacking Assignment
# For unpacking assignment, lengths at both sides must be the same
# Both left and right expression side brackets are optional
# Unpacking nested sequences
# Skipping values is done by using _