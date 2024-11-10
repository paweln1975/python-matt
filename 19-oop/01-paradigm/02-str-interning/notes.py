#!/usr/bin/env python3

# Reference:
# https://python3.info/oop/paradigm/str-interning.html

#%% String Interning
# Method of storing only one copy of each distinct string value, which must be immutable
# many high level languages use it
# string literals and values are internally kept in a hashed list called 'string intern pool' and those which are identical are rendered as references to the same object
# possible because str are immutable
# implementation dependent
# Jython, IronPython, PyPy and others may intern more aggressively
# Calling the intern() function on strings will "force" a string to have the same object identity as any equivalent and previously interned string
# https://en.wikipedia.org/wiki/String_interning