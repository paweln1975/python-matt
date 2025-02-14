"""
Name: Math Trigonometry Deg2Rad
Difficulty: easy
Lines: 10
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

>>> result_sin
0.02
>>> result_cos
1.0
>>> result_tg
0.02
>>> result_ctg
57.29
>>> result_pi
3.14

"""

# %% SetUp

from unittest.mock import MagicMock
import math

result_sin: float
result_cos: float
result_tg: float
result_ctg: float
result_pi: float

PRECISION = 2

input = MagicMock(side_effect=['1'])
degrees = input('What is the angle [deg]?: ')

# English
# 1. Read input (angle in degrees) from user
# 2. User will type `int` or `float`
# 3. Print all trigonometric functions (sin, cos, tg, ctg)
# 4. If there is no value for this angle, raise an exception
# 5. Round results to two decimal places
# 6. Run doctests - all must succeed

# Polish
# 1. Program wczytuje od użytkownika wielkość kąta w stopniach
# 2. Użytkownik zawsze podaje `int` albo `float`
# 3. Wyświetl wartość funkcji trygonometrycznych (sin, cos, tg, ctg)
# 4. Jeżeli funkcja trygonometryczna nie istnieje dla danego kąta podnieś
#    stosowny wyjątek
# 5. Wyniki zaokrąglij do dwóch miejsc po przecinku
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result_sin = ...
result_cos = ...
result_tg = ...
result_ctg = ...
result_pi = ...