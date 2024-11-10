"""
* Assignment: Django Conf Version
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define variable `result: str` with Django version
    2. Version has to be in format `X.Y.Z`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienną `result: str` z wersją Django
    2. Wersja musi być w formacie `X.Y.Z`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert type(result) is not Ellipsis, \
    'Assign result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> result.startswith('5.0')
    True
"""

# Define variable `result: str` with Django version
# type: str
result = ...

