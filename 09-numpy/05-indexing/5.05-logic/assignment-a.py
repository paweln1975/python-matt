"""
Name: Numpy Logic Even
Difficulty: easy
Lines: 3
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

>>> assert data is not Ellipsis, \
'Assign result to variable: `data`'
>>> assert type(data) is np.ndarray, \
'Variable `data` has invalid type, expected np.bool'

>>> assert result_a is not Ellipsis, \
'Assign result to variable: `result_a`'
>>> assert type(result_a) is np.bool, \
'Variable `result_a` has invalid type, expected np.bool'

>>> assert result_b is not Ellipsis, \
'Assign result to variable: `result_b`'
>>> assert type(result_b) is np.bool, \
'Variable `result_b` has invalid type, expected np.bool'

>>> data
array([ True, False, False, False, False, False, False, False,  True])

>>> result_a
np.False_

>>> result_b
np.True_

"""

# %% SetUp

import numpy as np

data: np.ndarray
result_a: np.ndarray
result_b: np.ndarray

np.random.seed(0)

DATA = np.random.randint(0, 100, size=9)

# English
# 1. Set random seed to zero
# 3. Check for even numbers of `DATA` which are less than 50 and save result to `data`
# 4. Check if all `data` matches this condition, result assing to `result_all`
# 5. Check if any `data` matches this condition, result assign to `result_any`
# 6. Run doctests - all must succeed

# Polish
# 1. Ustaw ziarno losowości na zero
# 3. Sprawdź parzyste elementy `DATA`, które są mniejsze od 50 i wynik zapisz do `data`
# 4. Sprawdź czy wszystkie `result` spełniają ten warunek, wynik zapisz do `result_all`
# 5. Sprawdź czy jakakolwiek `result` spełnia ten warunek, wynik zapisz do `result_any`
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
data = ...
result_a = ...
result_b = ...