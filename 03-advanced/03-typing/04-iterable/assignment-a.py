"""
* Assignment: Typing Annotations Tuple
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

    >>> assert annotations['a'] == tuple
    >>> assert annotations['b'] == tuple[int,...]
    >>> assert annotations['c'] == tuple[int,float,str]

    >>> assert a == (), \
    'Do not modify variable `a` value, just add type annotation'
    >>> assert b == (1, 2, 3), \
    'Do not modify variable `b` value, just add type annotation'
    >>> assert c == (1, 2.0, 'three'), \
    'Do not modify variable `c` value, just add type annotation'
"""

# Add type annotations to variables
a = ()
b = (1, 2, 3)
c = (1, 2.0, 'three')

