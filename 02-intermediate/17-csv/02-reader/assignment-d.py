
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
[('Mark', 'Watney', 'staff'),
 ('Melissa', 'Lewis', 'admins'),
 ('Rick', 'Martinez', 'staff'),
 ('Alex', 'Vogel', 'users'),
 ('Beth', 'Johanssen', 'staff'),
 ('Chris', 'Beck', 'staff')]
"""
# endregion

# region Show Imports
import csv
# endregion

# region Show Types
result: list[tuple[str,str,str]]
# endregion

FILE = r'_temporary.csv'

DATA = """
6,2,users,staff,admins
Mark,Watney,1
Melissa,Lewis,2
Rick,Martinez,1
Alex,Vogel,0
Beth,Johanssen,1
Chris,Beck,1
"""

with open(FILE, mode='wt', encoding='utf-8') as file:
    file.write(DATA.lstrip())

# English
# 1. Using `csv.reader()` read data from `FILE`
# 2. Define `result: list[tuple]` with converted data
# 3. Use Unix `\n` line terminator
# 4. Run doctests - all must succeed

# Polish
# 1. Za pomocą `csv.reader()` wczytaj dane z `FILE`
# 2. Zdefiniuj `result: list[tuple]` z przekonwertowanymi danymi
# 3. Użyj zakończenia linii Unix `\n`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code
result = []
with open(FILE, mode='rt', encoding='utf-8') as file:
    reader = csv.reader(file, lineterminator='\n', delimiter=',')
    nrows, ncols, *groups = next(reader)
    group_encoder = dict(enumerate(groups))

    for line in reader:
        firstname, lastname, group = line
        result.append((firstname, lastname, group_encoder[int(group)]))
