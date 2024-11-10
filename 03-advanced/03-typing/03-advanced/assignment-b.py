"""
* Assignment: Typing Annotations Optional
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Declare type for `data` variable
    2. Type must match values defined below
    3. Use union sytnax
    4. Run doctests - all must succeed

Polish:
    1. Zadeklaruj typ dla zmiennej `data`
    2. Typ musi pasować do wartości zdefiniowanych poniżej
    3. Użyj notacji unii
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert sys.version_info >= (3, 10), \
    'Python 3.10+ required'

    >>> import importlib
    >>> from typing import get_type_hints
    >>> module = importlib.import_module(__name__)
    >>> annotations = get_type_hints(module)

    >>> assert annotations['data'] == int | None
    >>> assert data is None, \
    'Do not modify variable `data` value, just add type annotation'
"""

# Declare type for `data` variable
# Type must match values defined below
# Use union sytnax
data: ...

# Do not modify lines below
data = 1
data = None

