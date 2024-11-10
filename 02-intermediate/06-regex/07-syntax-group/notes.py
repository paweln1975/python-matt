#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/regex/syntax-group.html

#%% Regex Syntax Group
# Catch expression results
# Can be named or positional
# (...) - unnamed group
# (?P<mygroup>...) - named group mygroup
# (?:...) - non-capturing group
# (?#...) - comment



#%% Positional Group
# (...) - unnamed (positional) group
# Used when you want to extract specific information from a text



#%% Named Group
# (?P<mygroup>...) - named group
# Used when you want to extract specific information from a text



#%% Non-Capturing Group
# (?:...) - non-capturing group
# Discard the group from the results
# Used when you want to use parentheses to group a part of the regular expression



#%% Comment
# (?#...) - comment
# Comments are ignored by the regex engine