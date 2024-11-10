"""
* Assignment: RE Match Phones
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Define `cell: str` pattern matching `+## ### ### ###`
    2. Define `work: str` pattern matching `+## ## ### ####`
    3. Define `result: str` matching a `cell` or `work` format
    4. Where `#` is a digit
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `cell: str` pasujący do `+## ### ### ###`
    2. Zdefiniuj `work: str` pasujący do `+## ## ### ####`
    3. Zdefiniuj `result: str` chwytającym format `cell` lub `work`
    4. Gdzie `#` jest cyfrą
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Use f-string formatting to combine both formats
    * Use alternative `|` inside of round brackets `(...|...)`
    * Use begining `^` and end `$` of a line

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> def is_valid_phone(number):
    ...     if re.match(result, number):
    ...         return True
    ...     else:
    ...         return False

    >>> is_valid_phone('+48 (12) 355 5678')
    False
    >>> is_valid_phone('+48 123 555 678')
    True
    >>> is_valid_phone('123 555 678')
    False
    >>> is_valid_phone('+48 12 355 5678')
    True
    >>> is_valid_phone('+48 123-555-678')
    False
    >>> is_valid_phone('+48 123 555 6789')
    False
    >>> is_valid_phone('+1 (123) 555-6789')
    False
    >>> is_valid_phone('+1 (123).555.6789')
    False
    >>> is_valid_phone('+1 800-python')
    False
    >>> is_valid_phone('+48123555678')
    False
    >>> is_valid_phone('+48 123 555 678 wew. 1337')
    False
    >>> is_valid_phone('+48 123555678,1')
    False
    >>> is_valid_phone('+48 123555678,1,2,3')
    False
"""

import re


# pattern matching `+## ### ### ###`
# type: str
cell = ...

# pattern matching `+## ## ### ####`
# type: str
work = ...

# combination of `+## ### ### ###` and `+## ## ### ####`
# type: str
result = ...


