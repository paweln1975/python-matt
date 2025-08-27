"""
Name: Pandas Read CSV Replace
Difficulty: easy
Lines: 5
Minutes: 8

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

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.DataFrame, \
'Variable `result` must be a `pd.DataFrame` type'
>>> assert len(result) == 25, \
'Select only 25 first rows'

>>> result.loc[[0,1,2,3,4,5], ['mean radius', 'mean texture', 'label']]
   mean radius  mean texture      label
0        17.99         10.38  malignant
1        20.57         17.77  malignant
2        19.69         21.25  malignant
3        11.42         20.38  malignant
4        20.29         14.34  malignant
5        12.45         15.70  malignant

>>> result['label'].value_counts()
label
malignant    22
benign        3
Name: count, dtype: int64

Hints:
`dict()`
`enumerate()`
`DataFrame.read_csv(nrows, names, skiprows)`
`DataFrame.replace(to_replace={'column': ...})`
`DataFrame.head(n)`

"""

# %% SetUp

import pandas as pd

result: pd.DataFrame

DATA = 'https://python3.info/_static/breast-cancer.csv'

COLUMNS = [
    'mean radius', 'mean texture', 'mean perimeter', 'mean area',
    'mean smoothness', 'mean compactness', 'mean concavity',
    'mean concave points', 'mean symmetry', 'mean fractal dimension',
    'radius error', 'texture error', 'perimeter error', 'area error',
    'smoothness error', 'compactness error', 'concavity error',
    'concave points error', 'symmetry error',
    'fractal dimension error', 'worst radius', 'worst texture',
    'worst perimeter', 'worst area', 'worst smoothness',
    'worst compactness', 'worst concavity', 'worst concave points',
    'worst symmetry', 'worst fractal dimension', 'label',
]

# English
# 1. Read data from `DATA` to `result: pd.DataFrame`
# 2. Use provided column names in `COLUMNS`
# 3. Read labels from the first row
# 4. Replace data in `label` column with values extracted above
# 5. Define `result: pd.DataFrame` with 25 first rows
# 6. Run doctests - all must succeed

# Polish
# 1. Wczytaj dane z `DATA` do `result: pd.DataFrame`
# 2. Użyj podanych w `COLUMNS` nazw kolumn
# 3. Wczytaj nazwy labeli z pierwszego wiersza
# 4. Podmień dane w kolumnie `label` na wartości wyciągnięte powyżej
# 5. Zdefiniuj `result: pd.DataFrame` z 25 pierwszymi wierszami
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
header = pd.read_csv(DATA, nrows=0)
nrows, nvalues, *labels = header.columns
decoder = dict(enumerate(labels))

print(decoder)
result = pd.read_csv(
    DATA,
    nrows=25,
    names=COLUMNS,
    skiprows=1,
).replace(to_replace={'label': decoder})