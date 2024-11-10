#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/star/assignment.html

#%% Star Assignment
# a, b, *c = 1, 2, 3, 4, 5
# Used when there is arbitrary number of values to unpack
# Could be used from start, middle, end
# There can't be multiple star expressions in one assignment statement
# _ is regular variable name, not a special Python syntax
# _ by convention is used for data we don't want to access in future



#%% Recap
# a = 1 - int
# a = 1, 2 - tuple
# a, b = 1, 2 - multiple assignment
# a, b, c = 1, 2, 3 - multiple assignment



#%% Arbitrary Number of Arguments
# Unpack values at the right side
# Unpack values at the left side
# Unpack values from both sides at once
# Unpack from variable length



#%% Errors
# Cannot unpack from both sides at once
# Unpack requires values for required arguments



#%% Skipping Values
# _ is used to skip values
# It is a regular variable name, not a special Python syntax
# By convention it is used for data we don't want to access in future
# It can be used multiple times in the same statement



#%% For Loop Unpacking
# Use star expression to unpack values in for loop



#%% Multi Dimensional
# Unpack values from multi-dimensional data