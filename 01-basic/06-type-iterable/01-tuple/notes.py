#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/type-iterable/tuple.html

#%% Iterable Tuple
# Immutable - cannot add, modify or remove items
# Stores elements of any type



#%% Syntax
# data = () - empty tuple
# data = (1, 2.2, 'abc') - tuple with values
# data = () is faster than data = tuple()

data = ()  # 2x times faster


#%% Type Conversion
# tuple() - will convert its argument to tuple
# Takes one iterable as an argument
# Multiple arguments are not allowed

print(tuple('hello'))

#%% Optional Brackets
# data = (1) - int
# data = (1.) - float
# data = (1,) - tuple

# to nie nawiasy robią tuple tylko przecinki

print((1+5) * 2)  # 12
print((1+5,) * 2)  # (6, 6)

#%% Tuple or Int, Float, Str
# data = 1.5 - float
# data = 1,5 - tuple
# data = (1) - int
# data = (1.) - float
# data = (1,) - tuple
# data = 1, - tuple



#%% Get Item
# Returns a value at given index
# Note, that Python start counting at zero (zero based indexing)
# Raises IndexError if the index is out of range
# More information in Unpack Getitem
# More information in Unpack Slice

data = 1, 2, 3
print(data[0])

#%% Index
# tuple.index() - position at which something is in the tuple
# Note, that Python start counting at zero (zero based indexing)
# Raises ValueError if the value is not present

print(data.index(2))  # Value 1, ValueError if not found

#%% Count
# tuple.count() - number of occurrences of value

print(data.count(1))

#%% Sort
# sorted() - return a new list containing all items from the iterable in ascending order
# Note, that the result will be a list, so we need to type cast
# Reverse flag can be set to request the result in descending order



#%% Length
# len() - Return the number of items in a container



#%% Built-in Functions
# min() - Minimal value
# max() - Maximal value
# sum() - Sum of elements
# len() - Length of a tuple
# all() - All values are True
# any() - Any values is True



#%% Memory
# Tuple is immutable (cannot be modified)
# Whole tuple must be defined at once
# Uses one consistent block of memory



#%% Recap
# Immutable - cannot add, modify or remove items
# Stores elements of any type
# Fast and memory efficient
