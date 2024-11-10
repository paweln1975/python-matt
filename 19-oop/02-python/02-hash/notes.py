#!/usr/bin/env python3

# Reference:
# https://python3.info/oop/python/hash.html

#%% OOP Hash
# Used for quickly compare two objects
# All objects compare unequal (except with themselves)
# set() elements has to be hashable
# dict() keys has to be hashable
# Used to quickly compare dictionary keys during a dictionary lookup
# Since Python 3.11: siphash13 is added as a new internal hashing algorithms. It has similar security properties as siphash24 but it is slightly faster for long inputs. str, bytes, and some other types now use it as default algorithm for hash() [#py311releasenotes]_



#%% Hash Method
# hash(obj) ->  int
# hash() returns the hash value of the object (if it has one)
# __hash__ should return the same value for objects that are equal
# User-defined classes have __eq__() and __hash__() methods by default
# It also shouldn't change over the lifetime of the object
# Generally you only implement it for immutable objects



#%% Set Definition



#%% Problem



#%% Hashable