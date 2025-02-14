
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
Mark,Watney,40
Melissa,Lewis,41
Rick,Martinez,39
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

class User:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

DATA = [
    User('Mark', 'Watney', age=40),
    User('Melissa', 'Lewis', age=41),
    User('Rick', 'Martinez', age=39),
    User('Alex', 'Vogel', age=42),
    User('Beth', 'Johanssen', age=29),
    User('Chris', 'Beck', age=36),
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
DATA = list(map(vars, DATA))
header = DATA[0].keys()
rows = [tuple(row.values()) for row in DATA]

with open(FILE, mode='wt', encoding='utf-8') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow(header)
    writer.writerows(rows)
