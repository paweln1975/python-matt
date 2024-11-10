"""
* Assignment: Mapping Dict Create
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Define `result: dict` with:
        a. key `firstname` with value `Mark`
        b. key `lastname` with value `Watney`
        c. key `group` with value `users`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: dict` z:
        a. kluczem `firstname` o wartości `Mark`
        b. kluczem `lastname` o wartości `Watney`
        c. kluczem `group` o wartości `users`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'

    >>> assert 'firstname' in result.keys(), \
    'Value `firstname` is not in the result keys'
    >>> assert 'lastname' in result.keys(), \
    'Value `lastname` is not in the result keys'
    >>> assert 'group' in result.keys(), \
    'Value `group` is not in the result keys'

    >>> assert 'Mark' in result['firstname'], \
    'Value `Mark` is not in the result values'
    >>> assert 'Watney' in result['lastname'], \
    'Value `Watney` is not in the result values'
    >>> assert 'users' in result['group'], \
    'Value `users` is not in the result values'
"""


# Define `result: dict` with:
# - key `firstname` with value `Mark`
# - key `lastname` with value `Watney`
# - key `group` with value `users`
# type: dict[str,str]
result = {
    'firstname': 'Mark',
    'lastname': 'Watney',
    'group': 'users'
}

