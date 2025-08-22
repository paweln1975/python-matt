"""
Name: Numpy Broadcasting Matmul
Difficulty: easy
Lines: 4
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

>>> mul_ab(a, b)  # doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
ValueError: operands could not be broadcast together with shapes (4,4) (4,2)

>>> matmul_ab(a, b)
array([[ 9,  2],
       [ 7,  3],
       [21,  8],
       [28,  8]])

>>> mul_ba(b, a)  # doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
ValueError: operands could not be broadcast together with shapes (4,2) (4,4)

>>> matmul_ba(b, a)
Traceback (most recent call last):
ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 4 is different from 2)

"""

# %% SetUp

import numpy as np

from typing import Callable
mul_ab: Callable[[np.ndarray, np.ndarray], np.ndarray|Exception]
matmul_ab: Callable[[np.ndarray, np.ndarray], np.ndarray|Exception]
mul_ba: Callable[[np.ndarray, np.ndarray], np.ndarray|Exception]
matmul_ba: Callable[[np.ndarray, np.ndarray], np.ndarray|Exception]

a = np.array([[1, 0, 1, 0],
              [0, 1, 1, 0],
              [3, 2, 1, 0],
              [4, 1, 2, 0]])

b = np.array([
    [4, 1],
    [2, 2],
    [5, 1],
    [2, 3]])

# English
# 1. For given: `a: np.ndarray`, `b: np.ndarray` (see below)
# 2. Multiply `a` and `b` using scalar multiplication
# 3. Multiply `a` and `b` using matrix multiplication
# 4. Multiply `b` and `a` using scalar multiplication
# 5. Multiply `b` and `a` using matrix multiplication
# 6. Discuss results
# 7. Run doctests - all must succeed

# Polish
# 1. Dla danych: `a: np.ndarray`, `b: np.ndarray` (patrz sekcja input)
# 2. Przemnóż `a` i `b` używając mnożenia skalarnego
# 3. Przemnóż `a` i `b` używając mnożenia macierzowego
# 4. Przemnóż `b` i `a` używając mnożenia skalarnego
# 5. Przemnóż `b` i `a` używając mnożenia macierzowego
# 6. Omów wyniki
# 7. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def mul_ab(a, b):
    return a * b

def matmul_ab(a, b):
    return np.matmul(a, b)

def mul_ba(b, a):
    return b * a

def matmul_ba(b, a):
    return np.matmul(b, a)
