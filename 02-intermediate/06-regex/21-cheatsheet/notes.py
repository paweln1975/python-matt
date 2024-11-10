#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/regex/cheatsheet.html

#%% Regex Cheatsheet
# Also known as: "Regular Expressions", "Regular Expr", "regexp", "regex" or "re"



#%% Syntax
# a - exact
# a|b - alternative
# [abc] - enumerated character class
# [a-z] - range character class
# . - any character except a newline (changes meaning with re.DOTALL)
# ^ - start of line (changes meaning with re.MULTILINE)
# $ - end of line (changes meaning with re.MULTILINE)
# \A - start of text (doesn't change meaning with re.MULTILINE)
# \Z - end of text (doesn't change meaning with re.MULTILINE)
# [^] - negation
# \d - digit (alias to [0-9])
# \D - anything but digit (alias to [^0-9])
# \s - whitespace (space, tab, newline, non-breaking space)
# \S - anything but whitespace
# \b - word boundary
# \B - anything but word boundary
# \w - any unicode alphabet character (lower or upper, also with diacritics (i.e. ąćęłńóśżź...), numbers and underscores
# \W - anything but any unicode alphabet character (i.e. whitespace, dots, comas, dashes)
# {n} - exactly n repetitions, exact
# {,n} - maximum n repetitions, greedy (prefer longest)
# {n,} - minimum n repetitions, greedy (prefer longest)
# {n,m} - minimum n repetitions, maximum m times, greedy (prefer longest)
# * - minimum 0 repetitions, no maximum, greedy (prefer longest), alias to {0,}
# + - minimum 1 repetitions, no maximum, greedy (prefer longest), alias to {1,}
# ? - minimum 0 repetitions, maximum 1 repetitions, greedy (prefer longest), alias to {0,1}
# {,n}? - maximum n repetitions, lazy (prefer shorter)
# {n,}? - minimum n repetitions, lazy (prefer shorter)
# {n,m}? - minimum n repetitions, maximum m times, lazy (prefer shorter)
# *? - minimum 0 repetitions, no maximum, lazy (prefer shorter), alias to {0,}?
# +? - minimum 1 repetitions, no maximum, lazy (prefer shorter), alias to {1,}?
# ?? - minimum 0 repetitions, maximum 1 repetition, lazy (prefer shorter), alias to {0,1}?
# () - matches whatever regular expression is inside the parentheses, and indicates the start and end of a group
# (...) - unnamed group (positional)
# (?P<mygroup>...) - named group mygroup
# (?:...) - non-capturing group
# (?#...) - comment
# (?P=name) - backreferencing by group name
# \g<number> - backreferencing by group number
# \g<name> - backreferencing by group name



#%% Python
# re.findall(pattern, text) - all occurrences of a pattern, results as a list[str]
# re.finditer(pattern, text) - all occurrences of a pattern, results as an Iterator[re.Match]
# re.search(pattern, text) - check if pattern is in the text (stops after first match), results as re.Match | None
# re.match(pattern, text) - checks if text matches pattern (validation, ie. email, ssn, tax id, phone), results as re.Match | None
# re.split(pattern, text) - split text by a pattern, results as a list[str]
# re.sub(pattern, replace, text) - replaces occurrences of a pattern in text with other text, results as a str
# re.compile(pattern) - prepare pattern for further use for example in a loop, results as a re.Pattern



#%% Flags
# re.ASCII - perform ASCII-only matching instead of full Unicode matching
# re.IGNORECASE - case-insensitive search
# re.MULTILINE - match can start in one line, and end in another
# re.DOTALL - dot (.) matches also newline characters
# re.UNICODE - turns on unicode character support for \w
# re.VERBOSE - ignores spaces (except \s) and allows for comments in in re.compile()
# re.DEBUG - display debugging information during pattern compilation