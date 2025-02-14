"""
Name: Math Statistics Iris
Difficulty: easy
Lines: 30
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result  # doctest: +NORMALIZE_WHITESPACE
{'virginica': {'sepal_length': {'values': [5.8, 6.3, 7.6, 4.9, 7.1, 6.5, 6.3],
                                'mean': 6.357142857142857,
                                'median': 6.3,
                                'stdev': 0.871506631944823,
                                'variance': 0.7595238095238092},
               'sepal_width': {'values': [2.7, 2.9, 3.0, 2.5, 3.0, 3.0, 3.3],
                               'mean': 2.914285714285714,
                               'median': 3.0,
                               'stdev': 0.25448360411214066,
                               'variance': 0.06476190476190473},
               'petal_length': {'values': [5.1, 5.6, 6.6, 4.5, 5.9, 5.8, 6.0],
                                'mean': 5.642857142857142,
                                'median': 5.8,
                                'stdev': 0.6754187413675136,
                                'variance': 0.45619047619047615},
               'petal_width': {'values': [1.9, 1.8, 2.1, 1.7, 2.1, 2.2, 2.5],
                               'mean': 2.0428571428571427,
                               'median': 2.1,
                               'stdev': 0.26992062325273125,
                               'variance': 0.07285714285714287}},
 'setosa': {'sepal_length': {'values': [5.1, 4.7, 4.9, 4.6, 5.4, 5.0, 4.6],
                             'mean': 4.9,
                             'median': 4.9,
                             'stdev': 0.2943920288775951,
                             'variance': 0.08666666666666677},
            'sepal_width': {'values': [3.5, 3.2, 3.0, 3.4, 3.9, 3.6, 3.1],
                            'mean': 3.3857142857142857,
                            'median': 3.4,
                            'stdev': 0.31320159337914943,
                            'variance': 0.09809523809523807},
            'petal_length': {'values': [1.4, 1.3, 1.4, 1.4, 1.7, 1.4, 1.5],
                             'mean': 1.4428571428571428,
                             'median': 1.4,
                             'stdev': 0.12724180205607036,
                             'variance': 0.01619047619047619},
            'petal_width': {'values': [0.2, 0.2, 0.2, 0.3, 0.4, 0.3, 0.2],
                            'mean': 0.2571428571428572,
                            'median': 0.2,
                            'stdev': 0.07867957924694431,
                            'variance': 0.006190476190476191}},
   'versicolor': {'sepal_length': {'values': [5.7, 6.4, 7.0, 5.7, 5.5, 6.5, 6.9],
                                   'mean': 6.242857142857143,
                                   'median': 6.4,
                                   'stdev': 0.6106202935189289,
                                   'variance': 0.3728571428571429},
                  'sepal_width': {'values': [2.8, 3.2, 3.2, 2.8, 2.3, 2.8, 3.1],
                                  'mean': 2.8857142857142857,
                                  'median': 2.8,
                                  'stdev': 0.31847852585154235,
                                  'variance': 0.10142857142857152},
                  'petal_length': {'values': [4.1, 4.5, 4.7, 4.5, 4.0, 4.6, 4.9],
                                   'mean': 4.4714285714285715,
                                   'median': 4.5,
                                   'stdev': 0.31997023671109237,
                                   'variance': 0.10238095238095248},
                  'petal_width': {'values': [1.3, 1.5, 1.4, 1.3, 1.3, 1.5, 1.5],
                                  'mean': 1.4,
                                  'median': 1.4,
                                  'stdev': 0.09999999999999998,
                                  'variance': 0.009999999999999995}}}

"""

# %% SetUp

from statistics import mean, stdev, median, variance

result: dict[str, dict]

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (7.1, 3.0, 5.9, 2.1, 'virginica'),
    (4.6, 3.4, 1.4, 0.3, 'setosa'),
    (5.4, 3.9, 1.7, 0.4, 'setosa'),
    (5.7, 2.8, 4.5, 1.3, 'versicolor'),
    (5.0, 3.6, 1.4, 0.3, 'setosa'),
    (5.5, 2.3, 4.0, 1.3, 'versicolor'),
    (6.5, 3.0, 5.8, 2.2, 'virginica'),
    (6.5, 2.8, 4.6, 1.5, 'versicolor'),
    (6.3, 3.3, 6.0, 2.5, 'virginica'),
    (6.9, 3.1, 4.9, 1.5, 'versicolor'),
    (4.6, 3.1, 1.5, 0.2, 'setosa'),
]

# English
# 1. Create dict `result: dict[str, dict]`
# 2. For each species calculate for numerical values:
#    - mean,
#    - median,
#    - standard deviation,
#    - variance.
# 3. Save data to `result` dict
# 4. Non-functional requirements:
#    - Use `statistics` module from Python standard library
# 5. Run doctests - all must succeed

# Polish
# 1. Stwórz słownik `result: dict[str, dict]`
# 2. Dla każdego gatunku wylicz dla wartości numerycznych:
#    - średnią,
#    - medianę,
#    - odchylenie standardowe,
#    - wariancję.
# 3. Dane zapisz w słowniku `result`
# 4. Wymagania niefunkcjonalne:
#    - Użyj modułu `statistics` z biblioteki standardowej Python
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...