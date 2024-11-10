#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/syntax/types.html

#%% Syntax Types
# int - Integer number
# float - Floating point number
# bool - Boolean value
# str - Character string
# None - Empty value (null)
# list - Ordered sequence of objects (can be modified)
# tuple - Ordered sequence of objects (cannot be modified)
# set - Unordered sequence of objects (can be modified)
# dict - Key-value data structure
# type() - Returns exact type of an argument
# isinstance() - Allows for checking if value is expected type



#%% Basic types
x = 1  # instancja klasy
x = 1.0
x = True
x = None # instancja klasy None type
print(type(x))
x = 'Hello world!'
x = [1, 2.0, 'hello']

def add(a, b):
    return a + b

print(add(1, 2))
print(add)  # zmienna wskazująca na adres w pamięci gdzie znajduje
print(type(add))  # instancja klasy function


#%% Sequences
x = (1, 2, 3)
x = {1, 2.0, 'hello'}
x = {'a':1, 'b':2.0, 'c':'hello'}


#%% Mappings
print(type(1))


#%% Type Checking
# type() - Returns type of an argument
# isinstance() - Allows for checking if value is expected type
# To check if type is what you expected use type() or isinstance()
# Later you will learn the difference

print(isinstance(1, int))
print(isinstance(1, float))
print(isinstance(1, int|float))
