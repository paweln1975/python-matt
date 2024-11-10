"""
* Assignment: Typing Annotations List of Dict
* Complexity: easy
* Lines of code: 2 lines
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

    >>> assert get_origin(annotations['data']) == list
    >>> assert data == [
    ...     {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
    ...     {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
    ...     {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'},
    ... ], \
    'Do not modify variable `data` value, just add type annotation'
"""

# Add type annotations to the variable
data = [
    {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
    {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
    {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'},
]

