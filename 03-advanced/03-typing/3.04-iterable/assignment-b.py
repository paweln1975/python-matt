"""
Name: Typing Annotations List
Difficulty: easy
Lines: 3
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

>>> import importlib
>>> from typing import get_type_hints
>>> module = importlib.import_module(__name__)
>>> annotations = get_type_hints(module)

>>> assert annotations['a'] == list
>>> assert annotations['b'] == list[int]
>>> assert annotations['c'] == list[int|float|str]

>>> assert a == [], \
'Do not modify variable `a` value, just add type annotation'
>>> assert b == [1, 2, 3], \
'Do not modify variable `b` value, just add type annotation'
>>> assert c == [1, 2.0, 'three'], \
'Do not modify variable `c` value, just add type annotation'

"""

# %% SetUp

# English
# 1. Add type annotations to variables
# 2. Run doctests - all must succeed

# Polish
# 1. Dodaj adnotacje typów do zmiennych
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
a: list = []
b: list[int] = [1, 2, 3]
c: list[int | float | str] = [1, 2.0, 'three']
