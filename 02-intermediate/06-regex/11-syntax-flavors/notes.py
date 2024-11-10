#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/regex/syntax-flavors.html

#%% Regex Syntax Flavors
# In other programming languages
# PCRE - Perl Compatible Regular Expressions



#%% Future
# Since Python 3.11
# Atomic grouping ((?>...)) and possessive quantifiers (*+, ++, ?+, {m,n}+) are now supported in regular expressions.
# https://www.regular-expressions.info/atomic.html
# https://github.com/python/cpython/issues/34627



#%% Enclosing
# In Python we use raw-string (r'...')
# In JavaScript we use /pattern/flags or new RegExp(pattern, flags)



#%% Flags
# In Python we use raw-string (r'...')
# In JavaScript we use /pattern/flags or new RegExp(pattern, flags)



#%% Named Ranges
# [:allnum:] - Alphabetic and numeric character [a-zA-Z0-9]
# [:alpha:] - Alphabetic character [a-zA-Z]
# [:alnum:] - Alphabetic and numeric character [a-zA-Z0-9]
# [:alpha:] - Alphabetic character [a-zA-Z]
# [:blank:] - Space or tab
# [:cntrl:] - Control character
# [:digit:] - Digit
# [:graph:] - Non-blank character (excludes spaces, control characters, and similar)
# [:lower:] - Lowercase alphabetical character
# [:print:] - Like [:graph:], but includes the space character
# [:punct:] - Punctuation character
# [:space:] - Whitespace character ([:blank:], newline, carriage return, etc.)
# [:upper:] - Uppercase alphabetical
# [:xdigit:] - Digit allowed in a hexadecimal number (i.e., 0-9a-fA-F)
# [:word:] - A character in one of the following Unicode general categories Letter, Mark, Number, Connector_Punctuation
# [:ascii:] - A character in the ASCII character set



#%% Range
# [a-Z] == [a-zA-Z]
# [a-9] == [a-zA-Z0-9]
# Works in other languages, but not in Python



#%% Group Backreference
# $1 - grep, egrep, Jetbrains IDE
# \1
# \g<1> - Python
# \g<name> - Python