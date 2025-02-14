"""
Name: Exception Assert Len
Difficulty: easy
Lines: 1
Minutes: 2

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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> check([1, 2, 3, 4, 5])
Traceback (most recent call last):
AssertionError
>>> check([1, 2, 3, 4])
Traceback (most recent call last):
AssertionError
>>> check([1, 2, 3])
>>> check([1, 2])
Traceback (most recent call last):
AssertionError
>>> check([1])
Traceback (most recent call last):
AssertionError
>>> check([])
Traceback (most recent call last):
AssertionError

Hints:
`assert`
`len()`

"""

# %% SetUp

from typing import Callable
check: Callable[[list|tuple], None]

# English
# 1. Check value passed to a `check` function:
#    - assert that argument `data` has length of 3
#    - if not, raise assertion error
# 2. Non-functional requirements:
#    - Write solution inside `check` function
#    - Mind the indentation level
#    - Use `assert` kyword
# 3. Run doctests - all must succeed

# Polish
# 1. Sprawdź poprawność wartości przekazanej do funckji `check`:
#    - zapewnij, że argument `data` ma długość 3
#    - jeżeli nie, podnieś błąd asercji
# 2. Wymagania niefunkcjonalne:
#    - Rozwiązanie zapisz wewnątrz funkcji `check`
#    - Zwróć uwagę na poziom wcięć
#    - Użyj słowa kluczowego `assert`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def check(data):
    ...