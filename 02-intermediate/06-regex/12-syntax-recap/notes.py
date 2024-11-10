#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/regex/syntax-recap.html

#%% Regex Recap



#%% Literals
# Also known as "Literal Characters"
# Occurrence of that character in the string



#%% Classes
# Also known as "Character Classes"
# One out of several characters



#%% Metacharacters
# Special characters



#%% Anchors
# Match a position before, after, or between characters



#%% Negation
# Negation logically inverts qualifier



#%% Shorthands
# Shorthand Character Classes



#%% Quantifiers
# Repetition
# How many occurrences of preceding token
# Exact - exactly number of times
# Greedy - prefer longest match, works better with numbers, (default)
# Lazy - prefer shortest matches - works better with text



#%% Groups
# Catch expression results
# Can be named or positional



#%% Backreference
# Match the same text as previously matched by a capturing group



#%% Flags
# re.ASCII - perform ASCII-only matching instead of full Unicode matching
# re.IGNORECASE - case-insensitive search
# re.LOCALE - case-insensitive matching dependent on the current locale (deprecated)
# re.MULTILINE - match can start in one line, and end in another
# re.DOTALL - dot (.) matches also newline characters
# re.UNICODE - turns on unicode character support for \w
# re.VERBOSE - ignores spaces (except \s) and allows for comments in in re.compile()
# re.DEBUG - display debugging information during pattern compilation



#%% Python
# re.findall() - all matches at once, returns list[str]
# re.finditer() - all matches one at a time, returns Iterator[re.Match]
# re.search() - whether text contains (stop after first match), returns re.Match | None
# re.match() - whether text matches pattern (validation, np. email, ssn, tax id, phone), returns re.Match | None
# re.split() - splits text by pattern, returns list[str]
# re.sub() - replaces group matches in text (works best with named groups), returns str
# re.compile() - prepares pattern for further use (match against it), returns re.Pattern