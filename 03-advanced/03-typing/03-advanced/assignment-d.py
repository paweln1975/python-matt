"""
* Assignment: Typing Annotations Literal
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Declare type for `data` variable
    2. Type must match values defined below
    3. Use `Literal` type
    4. Run doctests - all must succeed

Polish:
    1. Zadeklaruj typ dla zmiennej `data`
    2. Typ musi pasować do wartości zdefiniowanych poniżej
    3. Użyj typu `Literal`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert sys.version_info >= (3, 5), \
    'Python 3.5+ required'

    >>> import importlib
    >>> from typing import get_type_hints
    >>> module = importlib.import_module(__name__)
    >>> annotations = get_type_hints(module)

    >>> assert annotations['data'] == Literal['users', 'staff', 'admins']
"""

from typing import Literal


# Declare type for `data` variable
# Type must match values defined below
# Use `Literal` type
data: ...

# Do not modify lines below
data = 'users'
data = 'staff'
data = 'admins'


