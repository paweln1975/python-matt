#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/generator/expression.html

#%% Generator Expression
# Comprehensions executes instantly
# Comprehensions are stored in the memory until end of a program
# Comprehensions should be used when accessing values more than one
# Generator Expressions are lazy evaluated
# Generator Expressions are cleared once they are executed
# Generator Expressions should be used when accessing value once (for example in the loop)



#%% List Comprehension
# Comprehensions executes instantly
# Comprehensions will be in the memory until end of a program
# Comprehensions - Using values more than one



#%% Generator Expression
# Generators are lazy evaluated
# Creates generator object and assign reference
# Code is not executed instantly
# Sometimes code is not executed at all!
# Are cleared once they are executed
# Generator will calculate next number for every loop iteration
# Generator forgets previous number
# Generator doesn't know the next number
# It is used for one-time access to values (for example in the loop iterator)



#%% Comprehensions or Generator Expression
# If you need values evaluated instantly, there is no point in using generators



#%% Why Round Brackets?
# Round brackets does not produce tuples (commas does)
# Round brackets bounds context