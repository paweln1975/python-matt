#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/function/scope.html

#%% Function Scope
# Values defined in function does not leak out
# Functions has access to global values
# Shadowing is when you define variable with name identical to the one



#%% Values Leaking
# Values defined in function does not leak out



#%% Outer Scope
# Functions has access to global values



#%% Shadowing
# When variable in function has the same name as in outer scope
# Shadowing in a function is valid only in a function
# Shadowed variable will be deleted upon function return
# After function return, the original value of a shadowed variable



#%% Global
# global keyword allows modification of global variable
# Using global keyword is considered as a bad practice



#%% Global Scope



#%% Local Scope
# Variables defined inside function
# Variables are not available from outside
# If outside the function, will return the same as globals()



#%% Shadowing Global Scope
# Defining variable with the same name as in outer scope
# Shadowed variable will be deleted upon function return



#%% Builtins