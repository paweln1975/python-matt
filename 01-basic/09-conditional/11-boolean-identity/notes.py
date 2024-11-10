#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/conditional/boolean-identity.html

#%% Boolean Identity
# = assignment
# == checks for object equality
# is checks for object identity
# is compares id() output for both objects
# CPython: compares the memory address a object resides in
# Testing strings with is only works when the strings are interned



#%% Has Value



#%% Is Empty



#%% Is True of False
# True and False are singletons
# Comparing identity is faster
# Comparing values will yield the same result



#%% Is Numeric
# Type int caches value from -5 to 256
# For those values identity check is True
# For values lower than -5 or greater than 256 identity check is False



#%% Is String
# String instances differs
# You cannot compare their identity
# There is a caching mechanism in Python, which sometimes yield the same result
# In order to compare strings, you should compare their values, not identities



#%% Is Type or Instance
# type()
# isinstance()



#%% Performance
# Tested on Python 3.11.2