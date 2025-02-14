"""
Name: Syntax Exception Raise
Difficulty: easy
Lines: 2
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass

>>> isclass(NegativeKelvinError)
True
>>> issubclass(NegativeKelvinError, Exception)
True

>>> result(1)
>>> result(0)

>>> try:
...     result(-1)
... except NegativeKelvinError:
...     True
True

Hints:
`raise`
`if`

"""

# %% SetUp

from typing import Callable
result: Callable[[int], Exception]

class NegativeKelvinError(Exception):
    pass

# English
# 1. Check value `value` passed to a `result` function
# 2. If `value` is lower than 0, raise `NegativeKelvinError`
# 3. Run doctests - all must succeed

# Polish
# 1. Sprawdź wartość `value` przekazaną do funckji `result`
# 2. Jeżeli `value` jest mniejsze niż 0, podnieś `NegativeKelvinError`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def result(value):
    ...