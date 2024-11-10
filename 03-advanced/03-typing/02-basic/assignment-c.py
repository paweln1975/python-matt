"""
* Assignment: Typing Basic Logic
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

    >>> assert annotations['a'] == bool
    >>> assert annotations['b'] == bool
    >>> assert annotations['c'] == type(None)

    >>> assert a is True, \
    'Do not modify variable `a` value, just add type annotation'
    >>> assert b is False, \
    'Do not modify variable `b` value, just add type annotation'
    >>> assert c is None, \
    'Do not modify variable `c` value, just add type annotation'
"""

# Add type annotations to variables
a = True
b = False
c = None

