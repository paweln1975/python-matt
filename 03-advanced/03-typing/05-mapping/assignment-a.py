"""
* Assignment: Typing Annotations Mapping
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Add type annotations to variables
    2. Run doctests - all must succeed

Polish:
    1. Dodaj adnotacje typów do zmiennych
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert sys.version_info >= (3, 9), \
    'Python 3.9+ required'

    >>> import importlib
    >>> from typing import get_type_hints
    >>> module = importlib.import_module(__name__)
    >>> annotations = get_type_hints(module)

    >>> assert annotations['a'] == dict
    >>> assert annotations['b'] == dict[str, str]
    >>> assert annotations['c'] == dict[str, str | int]

    >>> assert a == {}, \
    'Do not modify variable `a` value, just add type annotation'
    >>> assert b == {'firstname': 'Mark', 'lastname': 'Watney'}, \
    'Do not modify variable `b` value, just add type annotation'
    >>> assert c == {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}, \
    'Do not modify variable `c` value, just add type annotation'
"""

# Add type annotations to variables
a = {}
b = {'firstname': 'Mark', 'lastname': 'Watney'}
c = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}

