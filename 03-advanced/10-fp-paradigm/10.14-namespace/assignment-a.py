"""
Name: Functional Closure Define
Difficulty: easy
Lines: 4
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert callable(check)
>>> assert callable(check(lambda:...))
>>> result = check(lambda:...).__call__()
>>> result is None
True

"""

# %% SetUp

from typing import Callable
check: Callable[[Callable], Callable]

# English
# 1. Define function `check` with `func: Callable` as a parameter
# 2. Define closure function `wrapper` inside `check`
# 3. Function `wrapper` takes `*args` and `**kwargs` as arguments
# 4. Function `wrapper` returns `None`
# 5. Function `check` must return `wrapper: Callable`
# 6. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj funkcję `check`, z `func: Callable` jako parametr
# 2. Zdefiniuj funkcję closure `wrapper` wewnątrz `check`
# 3. Funkcja `wrapper` przyjmuje `*args` i `**kwargs` jako argumenty
# 4. Funkcja `wrapper` zwraca `None`
# 5. Funkcja `check` ma zwracać `wrapper: Callable`
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def check(func: Callable):
    def wrapper(*args, **kwargs):
        pass
    return wrapper