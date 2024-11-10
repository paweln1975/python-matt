#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/type-string/input.html

#%% String Input
# input() always returns str
# Good practice: add space at the end of prompt
# Good practice: always .strip() text from user input
# Good practice: always sanitize values from user prompt



#%% Input Str

color = input('Podaj kolor: ')

#%% Input Int

age = input('Podaj wiek: ')
x = float(age.replace(',', '.')) > 10
print(x)

#%% Input Float



#%% Automated Input
# Stub - simple object which always returns the same result
# Mock - an object which has more advanced capabilities than Stub, such as:

from unittest.mock import Mock
input = Mock(side_effect=['Mark', 30])

firstname = input('Please provide a name: ')
age = input('Please provide your age: ')
print(firstname, age)

#%% Stub



#%% Mock
