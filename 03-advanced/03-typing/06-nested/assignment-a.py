"""
* Assignment: Typing Annotations List of Tuple
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Add type annotations to the variable
    2. Run doctests - all must succeed

Polish:
    1. Dodaj adnotacje typów do zmiennej
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert sys.version_info >= (3, 9), \
    'Python 3.9+ required'

    >>> import importlib
    >>> from typing import get_type_hints, get_origin
    >>> module = importlib.import_module(__name__)
    >>> annotations = get_type_hints(module)

    >>> assert annotations['data'] == list[list[int]]
    >>> assert get_origin(annotations['data']) == list
    >>> assert data == [
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9],
    ... ], \
    'Do not modify variable `data` value, just add type annotation'
"""

# Add type annotations to the variable
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

