
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result = open(FILE).read()
>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is str, \
'Variable `result` has invalid type, should be str'

>>> from os import remove
>>> remove(FILE)

>>> print(result)
firstname,lastname,age
Mark,Watney,42
Melissa,Lewis,41
Rick,Martinez,40
Alex,Vogel,42
Beth,Johanssen,29
Chris,Beck,36
<BLANKLINE>
"""
# endregion

# region Show Imports
import csv
# endregion

FILE = r'_temporary.csv'

DATA = [
    ('firstname', 'lastname', 'age'),
    ('Mark', 'Watney', 42),
    ('Melissa', 'Lewis', 41),
    ('Rick', 'Martinez', 40),
    ('Alex', 'Vogel', 42),
    ('Beth', 'Johanssen', 29),
    ('Chris', 'Beck', 36),
]

# English
# 1. Using `csv.writer()` save `DATA` to file
# 2. Use Unix `\n` line terminator
# 3. Run doctests - all must succeed

# Polish
# 1. Za pomocą `csv.writer()` zapisz `DATA` do pliku
# 2. Użyj zakończenia linii Unix `\n`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code

# old way
# with open(FILE, mode='wt', encoding='utf-8') as file:
#     result = []
#     for element in DATA:
#         name, lastname, age = element
#         result.append(f'{name},{lastname},{age}')
#     to_write = '\n'.join(result) + '\n'
#     file.write(to_write)


with open(FILE, mode='wt', encoding='utf-8') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(DATA)
