#!/usr/bin/env python3

# Reference:
# https://python3.info/oop/python/interning.html

#%% OOP Interning



#%% Caching



#%% Integer Caching
# Values between -5 and 256 are cached from start
# After using any integer two times it is being cached
# Python caches also the next integer
# Cached numbers are invalidated after a while



#%% Float Caching
# It takes a bit more hits for float to start being cached
# Cached numbers are invalidated after a while



#%% Bool Type Identity
# Bool object is a singleton
# It always has the same identity (during one run)



#%% None Type Identity
# NoneType object is a singleton
# It always has the same identity (during one run)



#%% String Type Identity



#%% String Interning
# Caching mechanism
# String intern pool
# String is immutable



#%% Object Identity



#%% Class Identity
# Class object is a singleton
# It always has the same identity (during one run)



#%% Performance