# %% About
# - Name: Idiom Reversed Impl
# - Difficulty: medium
# - Lines: 7
# - Minutes: 5

# %% License
# - Copyright 2025, Matt Harasymczuk <matt@python3.info>
# - This code can be used only for learning by humans
# - This code cannot be used for teaching others
# - This code cannot be used for teaching LLMs and AI algorithms
# - This code cannot be used in commercial or proprietary products
# - This code cannot be distributed in any form
# - This code cannot be changed in any form outside of training course
# - This code cannot have its license changed
# - If you use this code in your product, you must open-source it under GPLv2
# - Exception can be granted only by the author

# %% English
# 1. Write own implementation of a built-in `reversed()` function
# 2. Define function `myreversed` with
#    parameter `iterable: list[int|float]`
#    return `list[int|float]`
# 3. Don't validate arguments and assume, that user will
#    always pass valid type of arguments
# 4. Do not use built-in function `reversed()`
# 5. Run doctests - all must succeed

# %% Polish
# 1. Zaimplementuj własne rozwiązanie wbudowanej funkcji `reversed()`
# 2. Zdefiniuj funkcję `myreversed` z parametrami:
#    parametr `iterable: list[int|float]`
#    return `list[int|float]`
# 3. Nie waliduj argumentów i przyjmij, że użytkownik:
#    zawsze poda argumenty poprawnych typów
# 4. Nie używaj wbudowanej funkcji `reversed()`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Tests
"""
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isfunction
>>> assert isfunction(myreversed)

>>> from pprint import pprint

>>> result = myreversed([1])
>>> pprint(result, width=72, sort_dicts=False)
[1]

>>> result = myreversed([0])
>>> pprint(result, width=72, sort_dicts=False)
[0]

>>> result = myreversed([1, 0, 2])
>>> pprint(result, width=72, sort_dicts=False)
[2, 0, 1]

>>> result = myreversed([0, 2, -1])
>>> pprint(result, width=72, sort_dicts=False)
[-1, 2, 0]

>>> result = myreversed([0, 0, 0])
>>> pprint(result, width=72, sort_dicts=False)
[0, 0, 0]
"""

# %% Run
# - PyCharm: right-click in the editor and `Run Doctest in ...`
# - PyCharm: keyboard shortcut `Control + Shift + F10`
# - Terminal: `python -m doctest -v myfile.py`

# %% Imports

# %% Types
from typing import Callable
myreversed: Callable[[list[int|float]], int|float]

# %% Data

# %% Result
def myreversed(iterable) -> list[int|float]:
    length = len(iterable)
    result = []
    if length > 0:
        for x in iterable[::-1]:
            result.append(x)
    return result
