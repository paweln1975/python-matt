"""
* Assignment: Mapping Dict Getitem
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Use `DATA: dict`
    2. Define `result: str` with value for key 'firstname' from `DATA`
    3. Use getitem syntax
    4. Run doctests - all must succeed

Polish:
    1. Użyj `DATA: dict`
    2. Zdefiniuj `result: str` z wartością dla klucza 'firstname' z `DATA`
    3. Użyj składni getitem
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * dict[key]

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

# Define `result: str` with value for key 'firstname' from `DATA`
# Use getitem syntax
# type: str
result = DATA['firstname']

