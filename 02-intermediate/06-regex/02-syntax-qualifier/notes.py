#!/usr/bin/env python3

# Reference:
# https://python3.info/intermediate/regex/syntax-qualifier.html

#%% Regex Syntax Qualifier
# Qualifier specifies what to find.
# a - Exact
# a|b - Alternative
# [abc] - Enumeration
# [a-z] - Range



#%% Exact
# a - Exact



#%% Exact Alternate
# a|b - letter a or b (also works with expressions)



#%% Enumeration
# [abc] - letter a or b or c



#%% Range
# [a-z] - any lowercase ASCII letter from a to z
# [A-Z] - any uppercase ASCII letter from A to Z
# [0-9] - any digit from 0 to 9
# [a-zA-Z] - any ASCII letter from: a to z or from A to Z
# [A-z] - any ASCII letter from: a to z or from A to Z
# [a-zA-Z0-9] - any ASCII letter from a to z or from A to Z or digit from 0 to 9



#%% Joining
# [abc]|[123] - Enumeration alternative - letter a, b or c or digit 1, 2 3
# [a-z]|[0-9] - Range alternative - any lowercase ASCII letter from a to z or digit from 0 to 9