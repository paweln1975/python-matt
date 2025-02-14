"""
Name: Accessor Property Setter
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> pt = Point()

>>> pt.position = 1, 2, 3
>>> assert pt.x == 1
>>> assert pt.y == 2
>>> assert pt.z == 3

>>> pt.position = (4, 5, 6)
>>> assert pt.x == 4
>>> assert pt.y == 5
>>> assert pt.z == 6

>>> pt.position = [7, 8, 9]
>>> assert pt.x == 7
>>> assert pt.y == 8
>>> assert pt.z == 9

>>> pt.position = {'a':1, 'b':2, 'c':3}
Traceback (most recent call last):
TypeError

>>> pt.position = 1, 2
Traceback (most recent call last):
ValueError

"""

# %% SetUp

from typing import Callable
Point: type
position: Callable[[object, list|tuple|set], None]

# English
# 1. Define class `Point` with:
#    - Attribute `x: int`
#    - Attribute `y: int`
#    - Attribute `z: int`
#    - Property `position`
# 2. Setting `position`:
#    - If argument is not list, tuple, set raise Type Error
#    - If argument has length other than 3, raise Value
#    - Else sets `x`, `y`, `z` attributes from sequence
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasę `Point` z:
#    - Atrybut `x: int`
#    - Atrybut `y: int`
#    - Atrybut `z: int`
#    - Property `position`
# 2. Ustawianie `position`:
#    - Jeżeli argument nie jest list, tuple, set podnieś TypeError
#    - Jeżeli argument nie ma długości 3, podnieś ValueError
#    - W przeciwnym wypadku ustaw kolejne atrybuty `x`, `y`, `z` z sekwencji
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Point:
    x: int
    y: int
    z: int