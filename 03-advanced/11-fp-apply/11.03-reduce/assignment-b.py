"""
Name: Iterator Reduce Impl
Difficulty: medium
Lines: 5
Minutes: 13

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

>>> from inspect import isfunction
>>> from operator import add, mul
>>> assert isfunction(myreduce)

>>> myreduce(add, [1, 2, 3, 4, 5])
15

>>> myreduce(mul, [1, 2, 3, 4, 5])
120

"""

# %% SetUp

from typing import Callable
myreduce: Callable[[Callable, tuple|list], object]

# English
# 1. Write own implementation of a built-in `reduce()` function
# 2. Define function `myreduce` with parameters:
#    - parameter `function: Callable`
#    - parameter `iterable: list | tuple`
# 3. Don't validate arguments and assume, that user will:
#    - always pass valid type of arguments
#    - iterable length will always be greater than 0
# 4. Do not use: map, filter, zip, enumerate, all, any, reduce
# 5. Run doctests - all must succeed

# Polish
# 1. Zaimplementuj własne rozwiązanie wbudowanej funkcji `reduce()`
# 2. Zdefiniuj funkcję `myreduce` z parametrami:
#    - parameter `function: Callable`
#    - parameter `iterable: list | tuple`
# 3. Nie waliduj argumentów i przyjmij, że użytkownik:
#    - zawsze poda argumenty poprawnych typów
#    - długość iterable będzie większa od 0
# 4. Nie używaj: map, filter, zip, enumerate, all, any, reduce
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def myreduce(function, iterable):
    ...