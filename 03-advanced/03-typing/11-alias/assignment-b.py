"""
* Assignment: Typing Alias TypeParameters
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Modify definition of a function `add`
    2. Refactor type definition using Python 3.12 syntax,
       example: `def run[T: int](a: T, b: T) -> T: ...`
    3. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj definicję funkcji `add`
    2. Zrefaktoruj definiowanie typu używając składni Python 3.12,
       przykład: `def run[T: int](a: T, b: T) -> T: ...`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert sys.version_info >= (3, 12), \
    'Python 3.12+ required'

    >>> from typing import get_type_hints
    >>> get_type_hints(add)
    {'a': T, 'b': T, 'return': T}
"""

# Define type `T` to annotate variables
# Use `type` keyword and union syntax
def add(a: int | float, b: int | float) -> int | float:
    return a + b

