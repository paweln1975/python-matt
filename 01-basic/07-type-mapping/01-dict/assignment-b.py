"""
* Assignment: Mapping Dict ListOfPairs
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Use `DATA: list[tuple]`
    2. Define `result: dict` with `DATA` converted to `dict`
    3. Run doctests - all must succeed

Polish:
    1. Użyj `DATA: list[tuple]`
    2. Zdefiniuj `result: dict` z przekonwertowanym `DATA` do `dict`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * dict()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'

    >>> assert all(type(x) is str for x in result.keys()), \
    'All dict keys should be str'

    >>> assert 'firstname' in result.keys()
    >>> assert 'lastname' in result.keys()
    >>> assert 'group' in result.keys()

    >>> assert 'Mark' in result.values()
    >>> assert 'Watney' in result.values()
    >>> assert 'users' in result.values()

    >>> pprint(result, width=40, sort_dicts=False)
    {'firstname': 'Mark',
     'lastname': 'Watney',
     'group': 'users'}
"""

DATA = [
    ('firstname', 'Mark'),
    ('lastname', 'Watney'),
    ('group', 'users'),
]

# Define `result: dict` with `DATA` converted to `dict`
# type: dict[str,str]
result = dict(DATA)

