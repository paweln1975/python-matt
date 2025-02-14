"""
Name: Exception Assert Types
Difficulty: easy
Lines: 2
Minutes: 3

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> add_numbers(1, 0)
1
>>> add_numbers(0, 1)
1
>>> add_numbers(1.0, 0)
1.0
>>> add_numbers(0, 1.0)
1.0
>>> add_numbers('1', 0)
Traceback (most recent call last):
AssertionError: Parameter `a` must be int or float
>>> add_numbers(0, '1')
Traceback (most recent call last):
AssertionError: Parameter `b` must be int or float
>>> add_numbers([1], 0)
Traceback (most recent call last):
AssertionError: Parameter `a` must be int or float
>>> add_numbers(0, [1])
Traceback (most recent call last):
AssertionError: Parameter `b` must be int or float
>>> add_numbers(True, 0)
Traceback (most recent call last):
AssertionError: Parameter `a` must be int or float
>>> add_numbers(0, False)
Traceback (most recent call last):
AssertionError: Parameter `b` must be int or float

Hints:
`assert`
`isinstance()`
`type()`

"""

# %% SetUp

from typing import Callable
add_numbers: Callable[[int, int], int]

# English
# 1. Check value passed to a `add_numbers` function:
#    - assert that type of `a` or `b` is int or float
#    - if not, raise assertion error with message:
#      'Parameter `a` must be int or float'
# 2. Non-functional requirements:
#    - Write solution inside `add_numbers` function
#    - Mind the indentation level
#    - Use `assert` kyword
# 3. Run doctests - all must succeed

# Polish
# 1. Sprawdź poprawność wartości przekazanej do funckji `add_numbers`:
#    - zapewnij, że typ `a` oraz `b` jest int lub float
#    - jeżeli nie, podnieś błąd asercji z komunikatem:
#      'Parameter `a` must be int or float'
# 2. Wymagania niefunkcjonalne:
#    - Rozwiązanie zapisz wewnątrz funkcji `add_numbers`
#    - Zwróć uwagę na poziom wcięć
#    - Użyj słowa kluczowego `assert`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def add_numbers(a, b):
    return a + b