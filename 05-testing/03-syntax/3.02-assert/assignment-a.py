"""
Name: Exception Assert Version
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result( (3,11) )
Traceback (most recent call last):
AssertionError: Python 3.13+ required

>>> result( (3,12) )
Traceback (most recent call last):
AssertionError: Python 3.13+ required

>>> result( (3,12,4) )
Traceback (most recent call last):
AssertionError: Python 3.13+ required

>>> result( (3,13) )
>>> result( (3,13,0) )
>>> result( (3,13,0,) )

>>> result( (3,14) )
>>> result( (3,14,0) )
>>> result( (3,14,0,'alpha') )
>>> result( (3,14,0,'beta') )
>>> result( (3,14,0,'rc') )

Hints:
`assert`
`>=`

"""

# %% SetUp

from typing import Callable
result: Callable[[tuple[int, int, int]], None]

REQUIRED_VERSION = (3, 13)

# English
# 1. Check value passed to a `result` function:
#    - Check if `version` is greater or equal to `REQUIRED_VERSION`
#    - If not, raise exception with message 'Python 3.13+ required'
# 2. Non-functional requirements:
#    - Write solution inside `result` function
#    - Mind the indentation level
#    - Use `assert` kyword
# 3. Run doctests - all must succeed

# Polish
# 1. Sprawdź poprawność wartości przekazanej do funckji `result`:
#    - Sprawdź czy `version` jest większe lub równe `REQUIRED_VERSION`
#    - Jeżeli nie, podnieś wyjątek z komunikatem 'Python 3.13+ required'
# 2. Wymagania niefunkcjonalne:
#    - Rozwiązanie zapisz wewnątrz funkcji `result`
#    - Zwróć uwagę na poziom wcięć
#    - Użyj słowa kluczowego `assert`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def result(version):
    ...