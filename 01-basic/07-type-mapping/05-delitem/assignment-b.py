"""
* Assignment: Mapping Dict Clear
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Use `DATA: dict`
    2. Define `result: None` with result of clearing all values
    3. Use `clear` method
    4. Run doctests - all must succeed

Polish:
    1. Użyj `DATA: dict`
    2. Zdefiniuj `result: None` z wynikiem wyczyszczenia wszystkich wartości
    3. Użyj metodę `clear`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * dict.clear()

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is None, \
    'Variable `result` has invalid type, should be dict'
    >>> assert type(DATA) is dict, \
    'Variable `DATA` has invalid type, should be dict'
    >>> assert DATA == {}, \
    'Variable `DATA` has not been cleared properly'

    >>> pprint(result)
    None
"""

DATA = {
    'firstname': 'Mark',
    'lastname': 'Watney',
    'group': 'users',
}

# Define `result: None` with result of clearing all values
# Use `clear` method
# type: None
result = DATA.clear()

