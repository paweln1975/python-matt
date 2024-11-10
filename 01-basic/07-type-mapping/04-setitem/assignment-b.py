"""
* Assignment: Mapping Dict Update
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Use `result: dict`
    2. Change value for key 'group' to 'admins'
    3. Use `update` method
    4. Run doctests - all must succeed

Polish:
    1. Użyj `result: dict`
    2. Zmień wartość dla klucza 'group' na 'admins'
    3. Użyj metody `update`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * dict.update(key=value)

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
    >>> assert 'users' not in result.values()
    >>> assert 'admins' in result.values()

    >>> pprint(result, width=40, sort_dicts=False)
    {'firstname': 'Mark',
     'lastname': 'Watney',
     'group': 'admins'}
"""

result = {
    'firstname': 'Mark',
    'lastname': 'Watney',
    'group': 'users',
}

# Change value for key 'group' to 'admins'
# Use `update` method
# type: dict[str,str]
result.update(group='admins')

