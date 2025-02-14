"""
Name: Generator Function Range
Difficulty: medium
Lines: 5
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isfunction, isgenerator, isgeneratorfunction
>>> assert isfunction(myrange)
>>> assert isgeneratorfunction(myrange)
>>> assert isgenerator(myrange(0,10))

>>> list(myrange(0, 10, 2))
[0, 2, 4, 6, 8]

>>> list(myrange(0, 5))
[0, 1, 2, 3, 4]

Hints:
https://github.com/python/cpython/blob/main/Objects/rangeobject.c

"""

# %% SetUp

from typing import Callable
myrange: Callable[[int,int,int], list[int]]

# English
# 1. Write own implementation of a built-in `range()` function
# 2. Define function `myrange` with parameters:
#    - parameter `start: int`
#    - parameter `stop: int`
#    - parameter `step: int`
# 3. Don't validate arguments and assume, that user will:
#    - always pass valid type of arguments
#    - never give only one argument
#    - arguments will be unsigned
# 4. Do not use built-in function `range()`
# 5. Run doctests - all must succeed

# Polish
# 1. Zaimplementuj własne rozwiązanie wbudowanej funkcji `range()`
# 2. Zdefiniuj funkcję `myrange` z parametrami:
#    - parameter `start: int`
#    - parameter `stop: int`
#    - parameter `step: int`
# 3. Nie waliduj argumentów i przyjmij, że użytkownik:
#    - zawsze poda argumenty poprawnych typów
#    - nigdy nie poda tylko jednego argumentu
#    - argumenty będą nieujemne
# 4. Nie używaj wbudowanej funkcji `range()`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def myrange(start, stop, step=1):
    ...