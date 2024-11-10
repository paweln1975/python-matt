"""
* Assignment: Loop Dict Label Encoder
* Type: homework
* Complexity: easy
* Lines of code: 9 lines
* Time: 13 min

English:
    1. Define:
        a. `features: list[tuple]` - list of values
        b. `labels: list[str]` - species
    2. Separate header from data
    3. For each row append to `features`, `labels`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj:
        a. `features: list[tuple]` - lista wartości
        b. `labels: list[str]` - gatunki
    2. Odseparuj nagłówek od danych
    3. Dla każdego wiersza dodawaj do `feature`, `labels`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert type(features) is list
    >>> assert type(labels) is list
    >>> assert all(type(x) is tuple for x in features)
    >>> assert all(type(x) is str for x in labels)

    >>> pprint(features)
    [(5.8, 2.7, 5.1, 1.9),
     (5.1, 3.5, 1.4, 0.2),
     (5.7, 2.8, 4.1, 1.3),
     (6.3, 2.9, 5.6, 1.8),
     (6.4, 3.2, 4.5, 1.5),
     (4.7, 3.2, 1.3, 0.2)]

    >>> pprint(labels)
    ['virginica', 'setosa', 'versicolor', 'virginica', 'versicolor', 'setosa']
"""

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

# Values from column 0-3 from DATA without header
# type: list[tuple]
features: list[tuple] = []

for data in DATA[1:]:
    features.append(data[:-1])

# species name from column 4 from DATA without header
# type: list[str]
labels = [data[4] for data in DATA[1:]]

