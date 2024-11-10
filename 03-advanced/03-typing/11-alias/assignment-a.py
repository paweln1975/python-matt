"""
* Assignment: Typing Alias TypeKeyword
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define type `T` to annotate variables
    2. Use `type` keyword and union syntax
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj typ `T` do anotacji zmiennych
    2. Użyj słowa kluczowego `type` oraz notacji unii
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


