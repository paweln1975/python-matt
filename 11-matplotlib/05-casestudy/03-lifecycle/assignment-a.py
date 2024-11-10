"""
* Assignment: Matplotlib Lifecycle
* Complexity: medium
* Lines of code: 20 lines
* Time: 21 min

English:
    1. Prepare similar plot for `DATA`
    2. Take into account only `sepal_length` and `species`
    3. `species` should be on `y` axis
    4. `sepal_length` should be on `x` axis
    5. Red marker describes mean `sepal_length` for all species
    6. Run doctests - all must succeed

Polish:
    1. Opracuj podobny wykres dla danych `DATA`
    2. Weź pod uwagę jedynie `sepal_length` oraz `species`
    3. species ma być w osi `y`
    4. Na osi `x` ma być `sepal_length`
    5. Czerwony marker opisuje średnią długość `sepal_length` dla wszystkich gatunków
    6. Uruchom doctesty - wszystkie muszą się powieść
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


DATA = 'https://python3.info/_static/iris.csv'


