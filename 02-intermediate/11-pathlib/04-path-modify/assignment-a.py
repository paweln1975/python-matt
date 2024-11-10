"""
* Assignment: File Path Exception
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
   

Polish:
    1. Zdefiniuj:
        a. `result_a: bool` z wynikiem sprawdzenia czy ścieżka `a` istnieje
        b. `result_b: bool` z wynikiem sprawdzenia czy ścieżka `b` istnieje
    2. Użyj `Path` z `pathlib`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert result_a is not Ellipsis, \
    'Assign your result to function `result_a`'
    >>> assert result_b is not Ellipsis, \
    'Assign your result to function `result_b`'

    >>> result_a
    True

    >>> result_b
    False
"""

from pathlib import Path


a = Path.cwd()
b = Path.cwd() / 'notexisting.txt'


result_a = ...
result_b = ...


