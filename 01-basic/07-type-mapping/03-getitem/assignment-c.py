"""
* Assignment: Mapping Dict GetDefault
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Use `DATA: dict`
    2. Define `result: str` with value for key 'email'
    3. If value does not exist in dict, return 'n/a'
    4. Use `get` method with default value
    5. Run doctests - all must succeed

Polish:
    1. Użyj `DATA: dict`
    2. Zdefiniuj `result: str` z wartością dla klucza 'email'
    3. Jeżeli wartość nie istnieje w dict, zwróć 'n/a'
    4. Użyj metody `get` z wartością domyślną
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * dict.get(key, default)

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> pprint(result)
    'n/a'
"""

DATA = {
    'firstname': 'Mark',
    'lastname': 'Watney',
    'group': 'users',
}

# Define `result: str` with value for key 'email'
# If value does not exist in dict, return 'n/a'
# Use `get` method with default value
# type: str
result = DATA.get('email', 'n/a')

