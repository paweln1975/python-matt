#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/metaprogramming/new.html

#%% Metaprogramming New



#%% New Method
# Constructor method
# solely for creating the object
# cls as it's first parameter
# when calling __new__() you actually don't have an instance yet, therefore no self exists at that moment
# It takes the same arguments as __init__()



#%% Init Method
# Initializer method
# for initializing object with initial values
# self as it's first parameter
# __init__() is called after __new__() and the instance



#%% Return
# __new__() should return an instance of the class
# __init__() it called on a class returned by __new__()
# __init__() should return None



#%% Injecting New



#%% Do not Trigger Methods for User
# It is better when user can choose a moment when call .connect() method