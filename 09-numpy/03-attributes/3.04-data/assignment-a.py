"""
Name: Numpy Attributes
Difficulty: easy
Lines: 7
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

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is dict, \
'Variable `result` has invalid type, expected: dict'

>>> result  # doctest: +NORMALIZE_WHITESPACE
{'number of dimensions': 2,
 'number of elements': 6,
 'data type': dtype('float64'),
 'element size': 8,
 'shape': (2, 3),
 'strides': (24, 8)}

"""

# %% SetUp

import numpy as np

result: dict[str, int|tuple[int,...]|np.dtype]

DATA = np.array([[-1.1, 0.0, 1.1],
                 [2.2, 3.3, 4.4]])

# English
# 1. Define `result: dict` with:
#    - number of dimensions;
#    - number of elements;
#    - data type;
#    - element size;
#    - shape;
#    - strides.
# 2. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result: dict` z:
#    - liczbę wymiarów,
#    - liczbę elementów,
#    - typ danych,
#    - rozmiar elementu,
#    - kształt,
#    - przeskoki (strides).
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = {
    'number of dimensions': ...,
    'number of elements': ...,
    'data type': ...,
    'element size': ...,
    'shape': ...,
    'strides': ...,
}