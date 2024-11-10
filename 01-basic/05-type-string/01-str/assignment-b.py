"""
* Assignment: Type Str Quotes
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: str` with value:
       He said: "It's Monty Python"
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` z wartością:
       He said: "It's Monty Python"
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> print(result)
    He said: "It's Monty Python"
"""


# Define variable `result: str` with value:
# He said: "It's Monty Python"
# type: str
result = 'He said: "It\'s Monty Python"'

