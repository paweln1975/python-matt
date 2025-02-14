#!/usr/bin/env python3
# https://python3.info/advanced/oop-operator/about.html


# %% Operator About
# - Operator Overload
# - Operator Overload is the Pythonic way
# - Operator Overload allows readable syntax
# - Operator Overload allows simpler operations
# - All examples in this chapter uses dataclasses for you to focus on the important code, not boilerplate code just to make it works
# - https://github.com/python/cpython/blob/main/Grammar/python.gram#L695
# %%



# %% Operators
# - Source: https://github.com/python/cpython/blob/main/Grammar/python.gram#L695
# - Comparison: ==, !=, <=, <, >=, >, not in, in, is not, is
# - Bitwise: |, ^, &, <<, >>
# - Arithmetic: +, -, *, /, //, %, @, **, ~
# %%



# %% Recap
# %%



# %% Problem
# - Class 'Vector' does not define '__add__', so the '+' operator cannot be used on its instances
# - dataclass is used to generate __init__() and __repr__()
# - dataclass does not have any influence on addition
# %%



# %% Solution
# - Implement __add__() method
# - Takes two arguments, self and other
# - Other is another instance of the same class
# - Returns a new instance of the same class
# %%



# %% Further Reading
# - https://docs.python.org/reference/datamodel.html#emulating-numeric-types
# - https://docs.python.org/library/operator.html
# %%



