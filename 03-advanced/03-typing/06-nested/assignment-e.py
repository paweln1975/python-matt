"""
* Assignment: Typing Annotations Mapping
* Complexity: easy
* Lines of code: 3 lines
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
    ...     ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    ...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
    ...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
    ...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    ...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    ...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
    ... ], \
    'Do not modify variable `data` value, just add type annotation'
"""

# Add type annotations to the variable
data = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

