"""
* Assignment: Loop Dict LabelEncoder
* Type: homework
* Complexity: hard
* Lines of code: 14 lines
* Time: 13 min

English:
    1. Use `DATA: list[tuple]`
    2. Define `features: list` - list of values (data from columns 0-4)
    3. Define `labels: list` - species names encoded as integers (column 4)
    4. To encode and decode species generate from `DATA` two dictionaries:
        a. `decoder: dict` - eg. {0: 'virginica', 1: 'setosa', 2: 'versicolor'}
        b. `encoder: dict` - eg. {'virginica': 0, 'setosa': 1, 'versicolor': 2}
    5. Run doctests - all must succeed

Polish:
    1. Użyj `DATA: list[tuple]`
    2. Zdefiniuj `features: list` - lista wartości (dane z kolumn 0-4)
    3. Zdefiniuj `labels: list` - nazwy gatunków zakodowane jako liczby (kolumna 4)
    4. Aby móc zakodować i odkodować gatunki wygeneruj z `DATA` dwa słowniki:
        a. `decoder: dict` - np. {0: 'virginica', 1: 'setosa', 2: 'versicolor'}
        b. `encoder: dict` - np. {'virginica': 0, 'setosa': 1, 'versicolor': 2}
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert type(features) is list
    >>> assert type(labels) is list
    >>> assert all(type(x) is tuple for x in features)
    >>> assert all(type(x) is int for x in labels)

    >>> pprint(features)
    [(5.8, 2.7, 5.1, 1.9),
     (5.1, 3.5, 1.4, 0.2),
     (5.7, 2.8, 4.1, 1.3),
     (6.3, 2.9, 5.6, 1.8),
     (6.4, 3.2, 4.5, 1.5),
     (4.7, 3.2, 1.3, 0.2)]

    >>> pprint(labels)
    [0, 1, 2, 0, 2, 1]

    >>> decoder
    {0: 'virginica', 1: 'setosa', 2: 'versicolor'}

    >>> encoder
    {'virginica': 0, 'setosa': 1, 'versicolor': 2}
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

# my solution:

# Define `features: list` - list of values (data from columns 0-4)
# type: list[tuple]
header = DATA[0]
rows = DATA[1:]
features = [row[:-1] for row in rows]

# advanced
features = [tuple(values) for *values, species in rows]

# Generate `decoder: dict` - eg. {0: 'virginica', 1: 'setosa', 2: 'versicolor'}
# type: dict
decoder = {}
for *values, species in rows:
    if species not in decoder.values():
        decoder[len(decoder)] = species

# Generate `encoder: dict` - eg. {'virginica': 0, 'setosa': 1, 'versicolor': 2}
# type: dict
encoder = {}
for key, value in decoder.items():
    encoder[value] = key

# Define `labels: list` - species names encoded as integers (column 4)
# type: list[int]
labels = [encoder[species] for *values, species in rows]


# trainer solution
features = []
labels = []
decoder = {}
encoder = {}
i = 0

for row in DATA[1:]:
    values = row[0:4]
    species = row[4]
    if species not in encoder:
        decoder[i] = species
        encoder[species] = i
        i += 1
    labels.append(encoder[species])
    features.append(values)
