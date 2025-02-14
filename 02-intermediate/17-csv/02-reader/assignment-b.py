
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is list, \
'Variable `result` has invalid type, should be list'
>>> assert all(type(x) is tuple for x in result), \
'All rows in `result` should be tuple'

>>> from os import remove
>>> remove(FILE)

>>> from pprint import pprint
>>> pprint(result)
[('firstname', 'lastname', 'age'),
 ('Mark', 'Watney', '42'),
 ('Melissa', 'Lewis', '41'),
 ('Rick', 'Martinez', '40'),
 ('Alex', 'Vogel', '42'),
 ('Beth', 'Johanssen', '29'),
 ('Chris', 'Beck', '36')]
"""
# endregion

# region Show Imports
import csv
# endregion

# region Show Types
result: list[tuple[str,...]]
# endregion

FILE = r'_temporary.csv'

DATA = """
'firstname';'lastname';'age'
'Mark';'Watney';42
'Melissa';'Lewis';41
'Rick';'Martinez';40
'Alex';'Vogel';42
'Beth';'Johanssen';29
'Chris';'Beck';36
"""

with open(FILE, mode='wt', encoding='utf-8') as file:
    file.write(DATA.lstrip())

# English
# 1. Using `csv.reader()` read data from `FILE`
# 2. Define `result: list[tuple]` with converted data
# 3. Use Unix `\n` line terminator
# 4. Use delimiter `;`
# 5. Use quotechar `'`
# 6. Run doctests - all must succeed

# Polish
# 1. Używając `csv.reader()` wczytaj dane z `FILE`
# 2. Zdefiniuj `result: list[tuple]` z przekonwertowanymi danymi
# 3. Użyj zakończenia linii Unix `\n`
# 4. Użyj delimiter `;`
# 5. Użyj quotechar `'`
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code
with open(FILE, mode='rt', encoding='utf-8') as file:
    reader = csv.reader(file, lineterminator='\n', delimiter=';', quotechar="'")
    result = [tuple(line) for line in reader]
