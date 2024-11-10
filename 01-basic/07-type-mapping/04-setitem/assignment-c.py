"""
* Assignment: Mapping Dict UpdateMany
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Modify `result: dict`:
        a. change value for key 'firstname' to 'Melissa'
        b. change value for key 'lastname' to 'Lewis'
    2. Use `update` method
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj `result: dict`:
        a. zmień wartość dla klucza 'firstname' na 'Melissa'
        b. zmień wartość dla klucza 'lastname' na 'Lewis'
    2. Użyj metodę `update`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * dict.update()

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

    >>> assert 'Melissa' in result.values()
    >>> assert 'Lewis' in result.values()
    >>> assert 'users' in result.values()

    >>> pprint(result, width=40, sort_dicts=False)
    {'firstname': 'Melissa',
     'lastname': 'Lewis',
     'group': 'users'}
"""

result = {
    'firstname': 'Mark',
    'lastname': 'Watney',
    'group': 'users',
}

# Change value for key 'firstname' to 'Melissa'
# Change value for key 'lastname' to 'Lewis'
# Use `dict.update()` method
# type: dict[str,str]
result.update(firstname='Melissa', lastname='Lewis')

