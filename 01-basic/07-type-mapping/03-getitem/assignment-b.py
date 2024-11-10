"""
* Assignment: Mapping Dict Get
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Use `DATA: dict`
    2. Define `result: str` with value for key 'firstname'
    3. Use `get` method
    4. Run doctests - all must succeed

Polish:
    1. Użyj `DATA: dict`
    2. Zdefiniuj `result: str` z wartością dla klucza 'firstname'
    3. Użyj metodę `get`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * dict.get(key)

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> pprint(result)
    'Mark'
"""

DATA = {
    'firstname': 'Mark',
    'lastname': 'Watney',
    'group': 'users',
}

# Define `result: str` with value for key 'firstname'
# Use `get` method
# type: str
result = DATA.get('firstname')

