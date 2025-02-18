"""
Name: Typing Alias TypeParameters
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 12), \
'Python 3.12+ required'

>>> from typing import get_type_hints
>>> get_type_hints(add)
{'a': T, 'b': T, 'return': T}

"""

# %% SetUp

from typing import Callable

type T = int | float
add: Callable[[T, T], T]
# English
# 1. Modify definition of a function `add`
# 2. Refactor type definition using Python 3.12 syntax,
#    example: `def run[T: int](a: T, b: T) -> T: ...`
# 3. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj definicję funkcji `add`
# 2. Zrefaktoruj definiowanie typu używając składni Python 3.12,
#    przykład: `def run[T: int](a: T, b: T) -> T: ...`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result

def add(a: T, b: T) -> T:
    return a + b