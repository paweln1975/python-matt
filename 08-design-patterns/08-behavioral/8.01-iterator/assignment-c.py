"""
Name: Protocol Iterator Range
Difficulty: medium
Lines: 9
Minutes: 8

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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass, ismethod

>>> assert isclass(Range)

>>> r = Range(0, 0, 0)
>>> assert hasattr(r, '__iter__')
>>> assert hasattr(r, '__next__')
>>> assert ismethod(r.__iter__)
>>> assert ismethod(r.__next__)

>>> list(Range(0, 10, 2))
[0, 2, 4, 6, 8]

>>> list(Range(0, 5))
[0, 1, 2, 3, 4]

"""

# %% SetUp

from dataclasses import dataclass

from typing import Callable
Range: type
__iter__: Callable[[object], object]
__next__: Callable[[object], int]

# English
# 1. Modify class `Range` to write own implementation
#    of a built-in `range(start, stop, step)` function
# 2. Assume, that user will never give only one argument;
#    it will always be either two or three arguments
# 3. Use Iterator protocol
# 4. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `Range` aby napisać własną implementację
#    wbudowanej funkcji `range(start, stop, step)`
# 2. Przyjmij, że użytkownik nigdy nie poda tylko jednego argumentu;
#    zawsze będą to dwa lub trzy argumenty
# 3. Użyj protokołu Iterator
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class Range:
    start: int = 0
    stop: int = None
    step: int = 1