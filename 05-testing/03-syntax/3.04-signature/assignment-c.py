"""
Name: Star Signature Mixed
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
>>> from inspect import isfunction

>>> assert callable(compute)
>>> assert isfunction(compute)

>>> compute(1, 2, 3)
>>> compute(1, 2, 3, func=lambda:None)

>>> compute(1, 2)
Traceback (most recent call last):
TypeError: compute() missing 1 required positional argument: 'c'

>>> compute()  # doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
TypeError: compute() missing 3 required positional arguments: 'a', 'b',
and 'c'

>>> compute(1, 2, 3, lambda:None)
Traceback (most recent call last):
TypeError: compute() takes 3 positional arguments but 4 were given

>>> compute(a=1, b=2, c=3)  # doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
TypeError: compute() got some positional-only arguments passed as
keyword arguments: 'a, b, c'

"""

# %% SetUp

from typing import Callable
compute: Callable[[int,int,int,Callable],None]

# English
# 1. Create function `compute`, which always returns `None`
# 2. Function takes arguments:
#    - `a, b, c` - positional only
#    - `func` - keyword only
# 3. Run doctests - all must succeed

# Polish
# 1. Stwórz funkcję `compute`, która zawsze zwraca `None`
# 2. Funkcja przyjmuje argumenty:
#    - `a, b, c` - tylko pozycyjne
#    - `func` - tylko keyword
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def compute(a, b, c, func=lambda: ...):
    pass