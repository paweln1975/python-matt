"""
Name: Matplotlib Lifecycle
Difficulty: medium
Lines: 20
Minutes: 21

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

"""

# %% SetUp

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

DATA = 'https://python3.info/_static/iris.csv'

# English
# 1. Prepare similar plot for `DATA`
# 2. Take into account only `sepal_length` and `species`
# 3. `species` should be on `y` axis
# 4. `sepal_length` should be on `x` axis
# 5. Red marker describes mean `sepal_length` for all species
# 6. Run doctests - all must succeed

# Polish
# 1. Opracuj podobny wykres dla danych `DATA`
# 2. Weź pod uwagę jedynie `sepal_length` oraz `species`
# 3. species ma być w osi `y`
# 4. Na osi `x` ma być `sepal_length`
# 5. Czerwony marker opisuje średnią długość `sepal_length` dla wszystkich gatunków
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
