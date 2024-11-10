#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/regex/about.html

#%% Regex Syntax About
# Also known as Regular Expressions
# Also known as Regular Expr
# Also known as regexp
# Also known as regex
# Also known as re
# TEXT = 'Email from Mark Watney <mwatney@nasa.gov> received on: Sun, Jan 2nd, 2000 at 12:00 AM'
# https://www.youtube.com/watch?v=BmF-gEYXWVM&list=PLv4THqSPE6meFeo_jNLgUVKkP40UstIQv&index=3
# W3C HTML Email pattern: r"^[a-zA-Z0-9.!#$%&'*+/=?^_{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"



#%% Python
# import re
# re.findall() - find all occurrences of pattern in text, returns list[str]
# re.finditer() - find first occurrence of pattern in text, returns Iterator[re.Match]
# re.search() - find first occurrence of pattern in text, returns re.Match (stops after first match)
# re.match() - check if text matches pattern, used in validation: phone, email, tax id, etc., returns re.Match
# re.compile() - compile pattern into object for further use, for example in the loop, returns re.Pattern
# re.split() - split text by pattern, returns list[str]
# re.sub() - substitute pattern in text with something else, returns str



#%% Syntax
# Character Class - what to find (single character)
# Qualifiers - range to find (range)
# Negation
# Quantifiers - how many occurrences of preceding qualifier or character class
# Groups
# Look Ahead and Look Behind
# Flags
# Extensions
# [] - Qualifier
# {} - Quantifier
# () - Groups



#%% Escape characters
# Escape characters
# \t - tab
# \r - carriage return
# \n - newline
# \r\n - newline (on Windows)
# \b - backspace
# \v - vertical space
# \f - form feed
# \x - hexadecimal
# \o - octal
# \u - Unicode entity 16-bit
# \U - Unicode entity 32-bit
# \\ - backslash
# \' - apostrophe
# \" - double quote



#%% Raw Strings
# Recap information about raw strings r'...'
# Since Python 3.12 r-string is required https://docs.python.org/dev/whatsnew/3.12.html#other-language-changes



#%% ASCII vs Unicode
# re.UNICODE
# re.ASCII
# ASCII for letters in latin alphabet
# UNICODE includes diacritics and accent characters (ąśćłóźć, etc.)
# https://en.wikipedia.org/wiki/List_of_Unicode_characters
# https://symbl.cc/en/unicode-table/



#%% Digit, Hexadecimal, Octal



#%% Punctuation



#%% Visualization
# https://regexper.com/
# https://regex101.com/



#%% Further Reading
# https://www.youtube.com/watch?v=BmF-gEYXWVM&list=PLv4THqSPE6meFeo_jNLgUVKkP40UstIQv&index=3
# Kinsley, Harrison "Sentdex". Python 3 Programming Tutorial - Regular Expressions / Regex with re. Year: 2014. Retrieved: 2021-04-11. URL: https://www.youtube.com/watch?v=sZyAn2TW7GY
# https://www.rexegg.com/regex-trick-conditional-replacement.html
# https://www.rexegg.com/regex-lookarounds.html
# https://www.rexegg.com/regex-anchors.html#z