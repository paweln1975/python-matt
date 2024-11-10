#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/syntax/print.html

#%% Syntax Print
print('hello')
print("It's Monty Python")



#%% String
# Either quotes (") or apostrophes (') will work
# Pick one and be consistent
# Do not mix - str opening and closing characters must be the same
# More information in String Define
print("""It's \"Monty Python\"""")


#%% String Interpolation
# String interpolation will substitute variable
# More information in String Literals
name = 'Pawel'
firstname = 'Mark'
lastname = 'Watney'
print(f'Hello {name}')
print('Hello', name)

print('Hello ', firstname, ' ', lastname, '!', sep='')

# python way to go
print(f'Hello {firstname} {lastname}')

#%% Print
# Prints on the screen
# Print string
# Print variable
# Print formatted (interpolated) string
# More information in Builtin Printing

x = 'hello'
print(x)  # wyswietla hello czyli str(x)
print(repr(x))  # domyslnie tego używa Python Console

#%% Newlines
# Use \n for newline
# Do not add space after \n character
