"""
* Assignment: Mapping Dict Pop
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Use `DATA: dict`
    2. Define `result: str` with value popped for key 'group'
    3. Use `pop` method
    4. Run doctests - all must succeed

Polish:
    1. Użyj `DATA: dict`
    2. Zdefiniuj `result: str` z wartością dla klucza 'group'
    3. Użyj metodę `pop`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * dict.pop(key)

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> assert 'firstname' in DATA.keys()
    >>> assert 'lastname' in DATA.keys()
    >>> assert 'group' not in DATA.keys()

    >>> assert 'Mark' in DATA.values()
    >>> assert 'Watney' in DATA.values()
    >>> assert 'users' not in DATA.values()

    >>> pprint(result)
    'users'
"""

DATA = {
    'firstname': 'Mark',
    'lastname': 'Watney',
    'group': 'users',
}

# Define `result: str` with value popped for key 'group'
# Use `pop` method
# type: str
result = DATA.pop('group')

