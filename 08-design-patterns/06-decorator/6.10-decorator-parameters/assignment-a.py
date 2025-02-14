"""
Name: Decorator Arguments Syntax
Difficulty: easy
Lines: 5
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

>>> assert isfunction(result), \
'Create result() function'

>>> assert isfunction(result(1, 2)), \
'result() should take two positional arguments'

>>> assert isfunction(result(a=1, b=2)), \
'result() should take two keyword arguments: a and b'

>>> assert isfunction(result(a=1, b=2)(lambda: ...)), \
'result() should return decorator which can take a function as arg'

>>> @result(a=1, b=2)
... def echo(text):
...     return text

>>> echo('hello')
'hello'

"""

# %% SetUp

from typing import Callable
result: Callable[[int,int], Callable]

# English
# 1. Define decorator `result`
# 2. Decorator should take `a` and `b` as arguments
# 2. Define `wrapper` with `*args` and `**kwargs` parameters
# 3. Wrapper should call original function with its original parameters,
#    and return its value
# 4. Decorator should return `wrapper` function
# 5. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj dekorator `result`
# 2. Dekorator powinien przyjmować `a` i `b` jako argumenty
# 2. Zdefiniuj `wrapper` z parametrami `*args` i `**kwargs`
# 3. Wrapper powinien wywoływać oryginalną funkcję z jej oryginalnymi
#    parametrami i zwracać jej wartość
# 4. Decorator powinien zwracać funckję `wrapper`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def result():
    ...