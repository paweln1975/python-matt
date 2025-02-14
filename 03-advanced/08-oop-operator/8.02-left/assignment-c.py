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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert hasattr(Vector, '__matmul__'), \
'Class `Vector` has no `__matmul__` method'
>>> assert callable(Vector.__matmul__), \
'Class `Vector` has `__matmul__` attribute, which is not callable'

>>> a = Vector(x=1, y=2)
>>> b = Vector(x=3, y=4)
>>> result = a @ b

>>> print(result)
Vector(x=3, y=8)

Hints:
`object.__matmul__()`

"""

# %% SetUp

from dataclasses import dataclass

from typing import Callable
Vector: type
__matmul__: Callable[[object, object], object]

# English
# 1. Modify class `Vector`
# 2. Overload `@` operator to implement a scalar multiplication of vectors
# 3. Formula: `A@B = (A1*B1, A2*B2)`
# 4. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `Vector`
# 2. Przeciąż operator `@` aby zaimplementować mnożenie skalarne wektorów
# 3. Wzór: `A@B = (A1*B1, A2*B2)`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class Vector:
    x: int
    y: int