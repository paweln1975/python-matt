"""
Name: Operator Left Sub
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert hasattr(Vector, '__sub__'), \
'Class `Vector` has no `__sub__` method'
>>> assert callable(Vector.__sub__), \
'Class `Vector` has `__sub__` attribute, which is not callable'

>>> a = Vector(x=1, y=2)
>>> b = Vector(x=3, y=4)
>>> result = a - b

>>> print(result)
Vector(x=-2, y=-2)

Hints:
`object.__sub__()`

"""

# %% SetUp

from dataclasses import dataclass

from typing import Callable
Vector: type
__sub__: Callable[[object, object], object]

# English
# 1. Modify class `Vector`
# 2. Overload `-` operator to implement a subtraction of two vectors
# 3. Formula: `A-B = (Ax-Bx, Ay-By)`
# 4. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `Vector`
# 2. Przeciąż operator `-` aby zaimplementować odejmowanie dwóch wektorów
# 3. Wzór: `A-B = (Ax-Bx, Ay-By)`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class Vector:
    x: int
    y: int

    def __sub__(self, other):
        return Vector(x=self.x - other.x, y=self.y - other.y)