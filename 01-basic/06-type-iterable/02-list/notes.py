#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/type-iterable/list.html

#%% Iterable List
# Mutable - can add, remove, and modify items
# Stores elements of any type



#%% Syntax
# data = [] - empty list
# data = [1, 2.2, 'abc'] - list with values
# data = [] is faster than data = list()



#%% Type Conversion
# list() converts argument to list
# Takes one iterable as an argument
# Multiple arguments are not allowed



#%% Get Item
# Returns a value at given index
# Note, that Python start counting at zero (zero based indexing)
# Raises IndexError if the index is out of range
# More information in Unpack Getitem
# More information in Unpack Slice



#%% Set Item



#%% Del Item

data = [0, 1, 2, 3]
del data[0]  #  one possible way
print(data)

#%% Append
# list + list - add
# list += list - increment add
# list.extend() - extend  # interable
# list.append() - append  # takes one argument (object)
# O(1) complexity

result = data + ['x', 'y', 'z']
print(result)

#%% Insert
# list.insert(idx, object)
# Insert object at specific position
# O(n) complexity



#%% Sort
# sorted() - returns new sorted list, but does not modify the original
# list.sort() - sorts list and returns None



#%% Reverse
# list.reverse()



#%% Index
# list.index() - position at which something is in the list
# Note, that Python start counting at zero (zero based indexing)
# Raises ValueError if the value is not present

def hello():
    print('hello')

x = hello()
print(type(x))  # None Type, every function returns something, even None

#%% Count
# list.count() - number of occurrences of value



#%% Method Chaining



#%% Built-in Functions
# min() - Minimal value
# max() - Maximal value
# sum() - Sum of elements
# len() - Length of a list
# all() - All values are True
# any() - Any values is True



#%% Memory



#%% Shallow Copy vs Deep Copy
# Shallow Copy (by reference) - identifiers are pointing to the same object in memory
# Deep Copy - identifiers are pointing to distinct objects
# Shallow Copy is faster and requires less memory (no duplicated objects)
# Deep Copy is slower and requires twice sa much memory, but is safe for modification

data = ['a', 'b', 'c']
a = data  # shallow copy
b = data.copy()  # deep copy

#%% Recap
# Mutable - can add, remove, and modify items
# Stores elements of any type
# Extensible and flexible

print(dir(data))
