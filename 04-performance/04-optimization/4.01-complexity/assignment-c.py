"""
Name: Performance Compexity SplitTrainTest
Difficulty: easy
Lines: 4
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert type(features_train) is list, \
'make sure features_train is a list'

>>> assert type(features_test) is list, \
'make sure features_test is a list'

>>> assert type(labels_train) is list, \
'make sure labels_train is a list'

>>> assert type(labels_test) is list, \
'make sure labels_test is a list'

>>> assert all(type(x) is tuple for x in features_train), \
'all elements in features_train should be tuple'

>>> assert all(type(x) is tuple for x in features_test), \
'all elements in features_test should be tuple'

>>> assert all(type(x) is str for x in labels_train), \
'all elements in labels_train should be str'

>>> assert all(type(x) is str for x in labels_test), \
'all elements in labels_test should be str'

>>> features_train  # doctest: +NORMALIZE_WHITESPACE
[(5.8, 2.7, 5.1, 1.9),
 (5.1, 3.5, 1.4, 0.2),
 (5.7, 2.8, 4.1, 1.3),
 (6.3, 2.9, 5.6, 1.8),
 (6.4, 3.2, 4.5, 1.5),
 (4.7, 3.2, 1.3, 0.2)]

>>> features_test  # doctest: +NORMALIZE_WHITESPACE
[(7.0, 3.2, 4.7, 1.4),
 (7.6, 3.0, 6.6, 2.1),
 (4.9, 3.0, 1.4, 0.2),
 (4.9, 2.5, 4.5, 1.7)]

>>> labels_train
['virginica', 'setosa', 'versicolor', 'virginica', 'versicolor', 'setosa']

>>> labels_test
['versicolor', 'virginica', 'setosa', 'virginica']

"""

# %% SetUp

features_train: list[tuple]
features_test: list[tuple]
labels_train: list[str]
labels_test: list[str]

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
]

ratio = 0.6
header, *rows = DATA
split = int(len(rows) * ratio)

# English
# 1. Using List Comprehension split `DATA` into:
#    - `features_train: list[tuple]` - 60% of first features in `DATA`
#    - `features_test: list[tuple]` - 40% of last features in `DATA`
#    - `labels_train: list[str]` - 60% of first labels in `DATA`
#    - `labels_test: list[str]` - 40% of last labels in `DATA`
# 2. In order to do so, calculate pivot point:
#    - length of `DATA` times given percent (60% = 0.6)
#    - remember, that slice indicies must be `int`, not `float`
#    - for example: if dataset has 10 rows, then 6 rows will be for
#            training, and 4 rows for test
# 3. Run doctests - all must succeed

# Polish
# 1. Używając List Comprehension podziel `DATA` na:
#    - `features_train: list[tuple]` - 60% pierwszych features w `DATA`
#    - `features_test: list[tuple]` - 40% ostatnich features w `DATA`
#    - `labels_train: list[str]` - 60% pierwszych labels w `DATA`
#    - `labels_test: list[str]` - 40% ostatnich labels w `DATA`
# 2. Aby to zrobić, wylicz punkt podziału:
#    - długość `DATA` razy zadany procent (60% = 0.6)
#    - pamiętaj, że indeksy slice muszą być `int` a nie `float`
#    - na przykład: if zbiór danych ma 10 wierszy, to 6 wierszy będzie
#         do treningu, a 4 do testów
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
features_train = ...
features_test = ...
labels_train = ...
labels_test = ...