#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/type-iterable/set.html

#%% Iterable Set
# Only unique values
# Mutable - can add, remove, and modify items
# Stores only **hashable** elements (int, float, bool, None, str, tuple)
# Set is unordered data structure and do not record element position or insertion
# Do not support getitem and slice
# Contains in set has O(1) average case complexity [#pywikiTimeComplexity]_



#%% Syntax
# data = set() - empty set
# No short syntax
# Only unique values

data = {}  # to zrobi dict
data = set()
data = {1, 2, 3}
data = {1, 2, 3, 3}

print(data)

#%% Hashable
# Can store elements of any **hashable** types



#%% Type Conversion
# set() converts argument to set



#%% Deduplicate



#%% Add

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)

a |= b
print(a)

#%% Update

a.add(6)
print(a)

a.update({7, 8, 9})
print(a)

#%% Pop

print(dir(a))

#%% Membership



#%% Basic Operations



#%% Cardinality
