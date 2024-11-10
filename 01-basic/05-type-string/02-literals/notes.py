#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/type-string/literals.html

#%% String Literals



#%% Escape Characters
# \n - New line (ENTER)
# \t - Horizontal Tab (TAB)
# \' - Single quote ' (escape in single quoted strings)
# \" - Double quote " (escape in double quoted strings)
# \\ - Backslash \ (to indicate, that this is not escape char)
# More information in Builtin Printing
# https://en.wikipedia.org/wiki/List_of_Unicode_characters



#%% Unicode



#%% Format String
# String interpolation (variable substitution)
# Since Python 3.6
# Used for str concatenation

name = 'Mark'
result = f'Hello {name}'

#%% Unicode Literal
# In Python 3 str is Unicode
# In Python 2 str is Bytes
# In Python 3 u'...' is only for compatibility with Python 2

text = 'hello'  # unicode
text = b'hello'  # bytes
print(text)
text = u'hello'  # unicode

text = 'Paweł'
print(text.encode('utf-8'))

#%% Bytes Literal
# Used while reading from low level devices and drivers
# Used in sockets and HTTP connections
# bytes is a sequence of octets (integers between 0 and 255)
# bytes.decode() conversion to unicode str
# str.encode() conversion to bytes

text = b'Pawe\xc5\x82'
print(text.decode())

#%% Raw String
# Escapes does not matters

text = r'Hello\nWorld'
path = r'c:\Users\wz6l1y\OneDrive - Aptiv'
print(path)
