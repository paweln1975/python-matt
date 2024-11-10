"""
* Assignment: Mapping Dict KeysValuesItems
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Use `DATA: dict`
    2. Define variables:
        a. `result_a: list[str]` with keys from `DATA`
        b. `result_b: list[str]` with values from `DATA`
        c. `result_c: list[tuple]` with items from `DATA`
    3. Run doctests - all must succeed

Polish:
    1. Użyj `DATA: dict`
    2. Zdefiniuj zmienne:
        a. `result_a: list[str]` z kluczami z `DATA`
        b. `result_b: list[str]` z wartościami z `DATA`
        c. `result_c: list[tuple]` z elementami z `DATA`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * list()
    * dict.keys()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert type(result_a) is list, \
    'Variable `result_a` has invalid type, should be list'
    >>> assert all(type(x) is str for x in result_a), \
    'All elements in `result_a` should be str'

    >>> assert type(result_b) is list, \
    'Variable `result_b` has invalid type, should be list'
    >>> assert all(type(x) is str for x in result_b), \
    'All elements in `result_b` should be str'

    >>> assert type(result_c) is list, \
    'Variable `result_c` has invalid type, should be list'
    >>> assert all(type(x) is tuple for x in result_c), \
    'All elements in `result_c` should be tuple'

    >>> pprint(result_a)
    ['firstname', 'lastname', 'group']

    >>> pprint(result_b)
    ['Mark', 'Watney', 'users']

    >>> pprint(result_c, width=40)
    [('firstname', 'Mark'),
     ('lastname', 'Watney'),
     ('group', 'users')]
"""

DATA = {
    'firstname': 'Mark',
    'lastname': 'Watney',
    'group': 'users',
}

# Keys from `DATA`
# type: list[str]
result_a = list(DATA.keys())

# Values from `DATA`
# type: list[str]
result_b = list(DATA.values())

# Items from `DATA`
# type: list[tuple[str,str]]
result_c = list(DATA.items())

