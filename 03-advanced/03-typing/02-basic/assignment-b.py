"""
* Assignment: Typing Basic Float
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
    >>> assert sys.version_info >= (3, 5), \
    'Python 3.5+ required'

    >>> import importlib
    >>> from typing import get_type_hints
    >>> module = importlib.import_module(__name__)
    >>> annotations = get_type_hints(module)

    >>> assert annotations['a'] == float
    >>> assert annotations['b'] == float
    >>> assert annotations['c'] == float

    >>> assert a == 1.0, \
    'Do not modify variable `a` value, just add type annotation'
    >>> assert b == 0.0, \
    'Do not modify variable `b` value, just add type annotation'
    >>> assert c == -1.0, \
    'Do not modify variable `c` value, just add type annotation'
"""

# Add type annotations to variables
a = 1.0
b = 0.0
c = -1.0

