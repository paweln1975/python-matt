"""
* Assignment: Mapping Dict Union
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Use `DATA_A: dict`
    2. Use `DATA_B: dict`
    3. Define `result: dict` with union of `DATA_A` and `DATA_B`
    4. Run doctests - all must succeed

Polish:
    1. Użyj `DATA_A: dict`
    2. Użyj `DATA_B: dict`
    3. Zdefiniuj `result: dict` z unią `DATA_A` i `DATA_B`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * |

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> import string

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'

    >>> pprint(result, width=40, sort_dicts=True)
    {'botanist': 'Mark Watney',
     'chemist': 'Alex Vogel',
     'commander': 'Melissa Lewis',
     'engineer': 'Beth Johanssen',
     'pilot': 'Rick Martinez',
     'surgeon': 'Chris Beck'}
"""


DATA_A = {
    'commander': 'Melissa Lewis',
    'botanist': 'Mark Watney',
    'pilot': 'Rick Martinez',
}

DATA_B = {
    'chemist': 'Alex Vogel',
    'engineer': 'Beth Johanssen',
    'surgeon': 'Chris Beck',
}

# Define `result: dict` with union of `DATA_A` and `DATA_B`
# type: dict[str, str]
result = DATA_A | DATA_B

