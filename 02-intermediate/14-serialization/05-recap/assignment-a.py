
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> dump(DATA, file=FILE)
>>> result = open(FILE).read()

>>> from os import remove
>>> remove(FILE)

>>> assert type(result) is str, \
'Variable `result` has invalid type, should be str'
>>> assert result != '', \
'File content is empty'

>>> print(result)
"petal_length","petal_width","sepal_length","sepal_width","species"
"1.4","0.2","5.1","3.5","setosa"
"5.1","1.9","5.8","2.7","virginica"
"1.4","0.2","5.1","3.5","setosa"
"4.1","1.3","5.7","2.8","versicolor"
"5.6","1.8","6.3","2.9","virginica"
"4.5","1.5","6.4","3.2","versicolor"
<BLANKLINE>
"""
# endregion

# region Show Types
from typing import Callable
dump: Callable[[list[dict[str, float]], str], None]
# endregion

FILE = '_temporary.csv'

DATA = [
    {'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2, 'species': 'setosa'},
    {'sepal_length': 5.8, 'sepal_width': 2.7, 'petal_length': 5.1, 'petal_width': 1.9, 'species': 'virginica'},
    {'sepal_length': 5.1, 'sepal_width': 3.5, 'petal_length': 1.4, 'petal_width': 0.2, 'species': 'setosa'},
    {'sepal_length': 5.7, 'sepal_width': 2.8, 'petal_length': 4.1, 'petal_width': 1.3, 'species': 'versicolor'},
    {'sepal_length': 6.3, 'sepal_width': 2.9, 'petal_length': 5.6, 'petal_width': 1.8, 'species': 'virginica'},
    {'sepal_length': 6.4, 'sepal_width': 3.2, 'petal_length': 4.5, 'petal_width': 1.5, 'species': 'versicolor'},
]

# English
# 1. Define function `dump()`:
#    - Argument: `data: list[tuple]`, `file: str`
#    - Returns: `None`
#    - Function writes `data` to `file` in CSV format
#    - Add quotes to values
# 2. Sort header
# 3. Non-functional requirements:
#    - Do not use `import` and any module
#    - Quotechar: `"`
#    - Quoting: always
#    - Delimiter: `,`
#    - Lineseparator: `\n`
#    - Sort `fieldnames`
# 4. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj funkcję `dump()`:
#    - Argument: `data: list[tuple]`, `file: str`
#    - Zwraca: `None`
#    - Funkcja zapisuje `data` do `file` w formacie CSV
#    - Dodaj cudzysłowie do wartości
# 2. Posortuj header
# 3. Wymagania niefunkcjonalne:
#    - Nie używaj `import` ani żadnych modułów
#    - Quotechar: `"`
#    - Quoting: zawsze
#    - Delimiter: `,`
#    - Lineseparator: `\n`
#    - Posortuj `fieldnames`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# region Show Hints
# - `sorted()`
# - `str.join()`
# - `dict.get(..., default)`
# endregion

# %% Your code
def dumps(data):
    header = sorted(data[0].keys())
    header_list = [f'"{name}"' for name in header]

    data_rows = []
    for line in data:
        row = []
        for name in header:
            row.append(f'"{line.get(name)}"')
        data_rows.append(','.join(row))

    return ','.join(header_list) + '\n' + '\n'.join(data_rows)

def dump(data, file):
    with open(file, 'w') as f:
        data_to_write = dumps(data) + '\n'
        f.write(data_to_write)
