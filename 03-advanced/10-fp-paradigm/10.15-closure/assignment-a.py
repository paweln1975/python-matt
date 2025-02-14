"""
Name: Functional Closure Call
Difficulty: easy
Lines: 9
Minutes: 5

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

>>> assert isfunction(hello)
>>> assert isfunction(result)
>>> assert not hasattr(__name__, 'check')

>>> hello()
'hello from function'

>>> result()
'hello from wrapper'

>>> check()
Traceback (most recent call last):
NameError: name 'check' is not defined

"""

# %% SetUp

from typing import Callable
check: Callable[[Callable], Callable]
hello: Callable[[], str]
result: Callable[[], str]

def check():
    ...

def hello():
    ...

# English
# 1. Define function `check` with parameter `func: Callable`
# 2. Define closure function `wrapper` inside `check`
# 3. Function `wrapper` takes:
#    - arbitrary number of positional arguments
#    - arbitrary number of keyword arguments
# 4. Function `wrapper` returns 'hello from wrapper'
# 5. Function `check` must return `wrapper: Callable`
# 6. Define function `hello()` which returns 'hello from function'
# 7. Define `result` with result of calling `check(hello)`
# 8. Delete `check` using `del` keyword
# 9. Call `result`
# 10. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj funkcję `check` z parametrem `func: Callable`
# 2. Zdefiniuj funkcję closure `wrapper` wewnątrz `check`
# 3. Funkcja `wrapper` przyjmuje:
#    - dowolną ilość argumentów pozycyjnych
#    - dowolną ilość argumentów nazwanych
# 4. Funkcja `wrapper` zwraca 'hello from wrapper'
# 5. Funkcja `check` ma zwracać `wrapper: Callable`
# 6. Zdefiniuj funkcję `hello()`, która zwraca 'hello from function'
# 7. Zdefiniuj zmienną `result`, która jest wynikiem wywołania `check(hello)`
# 8. Skasuj `check` za pomocą słowa kluczowego `del`
# 9. Wywołaj `result`
# 10. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...