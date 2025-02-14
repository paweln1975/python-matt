"""
Name: Decorator Function Check
Difficulty: easy
Lines: 3
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

>>> from inspect import isfunction

>>> assert isfunction(check), \
'Create check() function'

>>> assert isfunction(check(lambda: ...)), \
'check() should take function as an argument'

>>> @check
... def echo(text):
...     print(text)

>>> assert isfunction(echo), \
'Decorator check() should return a function'

>>> echo.disabled = False
>>> echo('hello')
hello

>>> echo.disabled = True
>>> echo('hello')
Traceback (most recent call last):
PermissionError: Function is disabled

>>> assert hasattr(echo, 'disabled')

"""

# %% SetUp

from typing import Callable
check: Callable[[Callable], Callable]

# English
# 1. Create decorator `check`
# 2. Decorator calls function, only when `echo.disabled` is `False`
# 3. Note that decorators overwrite reference and in `wrapper`
#    you must check if `wrapper.disabled` is `False`
# 4. Else raise an exception `PermissionError`
# 5. Run doctests - all must succeed

# Polish
# 1. Stwórz dekorator `check`
# 2. Dekorator wywołuje funkcję, tylko gdy `echo.disabled` jest `False`
# 3. Zwróć uwagę, że dekoratory nadpisują referencje i we `wrapper`
#    musisz sprawdzić czy `wrapper.disabled` jest `False`
# 4. W przeciwnym przypadku podnieś wyjątek `PermissionError`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def check(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper