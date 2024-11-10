#!/usr/bin/env python3

# Reference:
# https://python3.info/basics/type-string/methods.html

#%% String Methods
# str is immutable
# str methods create a new modified str



#%% Strip Whitespace
# str.strip() - remove whitespaces from both ends
# str.lstrip() - remove whitespaces from left side only
# str.rstrip() - remove whitespaces from right side only



#%% Change Case
# str.upper() - all letters will be uppercase
# str.lower() - all letters will be lowercase
# str.capitalize() - will uppercase first letter of text, lowercase others
# str.title() - will uppercase first letter of each word, lowercase others
# str.swapcase() - make lowercase letters upper, and uppercase lower



#%% Replace
# str.replace()
# str.removesuffix()
# str.removeprefix()
# str.strip()



#%% Starts or Ends With
# str.startswith() - return True if str starts with the specified prefix, False otherwise
# str.endswith() - return True if str ends with the specified suffix, False otherwise
# optional start, test str beginning at that position
# optional end, stop comparing str at that position
# prefix/suffix can also be a tuple of strings to try

domains = ('nasa.gov', 'polsa.gov.pl')
x = 'mwatney@nasa.gov'

print(x.endswith(domains))

#%% Split by Line
# str.splitlines() - split by newline character, don't leave empty lines at the end
# str.split('\n') - will leave empty string if newline is a the end of str

TEXT = """One
Two
Three
"""

print(TEXT.splitlines())
print(TEXT.split("\n"))

#%% Split by Character
# str.split() - Split by given character
# No argument - any number of whitespaces



#%% Join by Character
# [#PyDocStrJoin]_
# str.join(sep, sequence) - concatenate sequence using separator
# Note, this is a method of a str, not tuple.join() or list.join()



#%% Join Numbers
# (str(x) for x in data) - using comprehension or generator expression
# map(str, data) - using map transformation
# Type cast won't work str(data) - it will stringify whole list



#%% Is Whitespace
# str.isspace() - Is whitespace (space, tab, newline)
#   - space
# \t - tab
# \n - newline



#%% Is Alphabet Characters
# text in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

import string
string.ascii_letters


#%% Is Numeric
# str.isdecimal()
# str.isdigit()
# str.isnumeric()
# str.isalnum()
# https://docs.python.org/library/stdtypes.html#str.isdecimal
# https://docs.python.org/library/stdtypes.html#str.isdigit
# https://docs.python.org/library/stdtypes.html#str.isnumeric
# https://docs.python.org/library/stdtypes.html#str.isalnum



#%% Find Sub-String Position
# str.find() - Finds position of a letter in text
# returns -1 if not found



#%% Count Occurrences
# str.count()
# returns 0 if not found



#%% Remove Prefix or Suffix
# str.removeprefix()
# str.removesuffix()
# Since Python 3.9: :pep:616 -- String methods to remove prefixes and suffixes



#%% Method Chaining
