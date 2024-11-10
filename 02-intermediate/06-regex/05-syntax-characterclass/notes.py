#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/regex/syntax-characterclass.html

#%% Regex Syntax CharacterClass
# Character Classes specifies what to find



#%% Numeric
# \d - digit
# \D - anything but digit



#%% Whitespaces
# \s - whitespace (space, tab, newline, non-breaking space)
# \S - anything but whitespace
# \n - newline
# \r\n - windows newline
# \r - carriage return
# \b - backspace
# \t - tab
# \v - vertical space
# \f - form feed



#%% Word Boundary
# Matches the empty string, but only at the beginning or end of a word
# \b - word boundary
# \B - anything but word boundary



#%% Word Character
# \w - any unicode alphabet character (lower or upper, also with diacritics (i.e. ąćęłńóśżź...), numbers and underscores
# \W - anything but any unicode alphabet character (i.e. whitespace, dots, comas, dashes)
# lowercase letters including diacritics (i.e. ąćęłńóśżź...) and accents
# uppercase letters including diacritics (i.e. ĄĆĘŁŃÓŚŻŹ...) and accents
# digits
# underscores _