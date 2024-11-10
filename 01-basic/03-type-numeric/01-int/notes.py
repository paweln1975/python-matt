#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/type-numeric/int.html

#%% Numeric Int
# Represents an integer
# Could be both signed and unsigned
# Default int size is 64 bit
# Python automatically extends int when need bigger number



#%% Syntax
# Signed and Unsigned
# Use _ for thousand separator

x = 1000000
x = 1_000_000
x = 1_000_000_000

#%% Thousands Separator
# You can use _ for easier read especially with big numbers



#%% Type Conversion
# Builtin function int() converts argument to int
# It is not rounding
# Works with strings, if all characters could be converted to int
# Supports only: +, - and _ (underscore)

int(2)  # to jest klasa

# class int:
#     def __init__(self, value):
#         self.value = value
#
#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls)
#         return instance

#%% Type Conversion Errors
# Works with strings, if all characters could be converted to int
# It is not validator or parser to extract all numbers from str

# int('a')  # Value Error, bo są jakieś stringi które się
# int([1, 2, 3])  # Type Error, bo żadnej listy nie da się skonfertować

int('0x1F', base=16)
hex(97)

print(ord('a'))

#%% Rounding
# Builtin function int() does not round numbers - only converts to int
# Use round() for numbers rounding

print(round(10.5))

#%% Homework
