
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
age,firstname,lastname
40,Mark,Watney
41,Melissa,Lewis
39,Rick,Martinez
<BLANKLINE>
"""
# endregion

# region Show Imports
import csv
# endregion

FILE = r'_temporary.txt'

class User:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

DATA = [
    User('Mark', 'Watney', age=40),
    User('Melissa', 'Lewis', age=41),
    User('Rick', 'Martinez', age=39),
]

# English
# 1. Using `csv.DictWriter()` save data to `FILE`
# 2. Non-functional requirements:
#    - Use `,` to separate columns
#    - Use `utf-8` encoding
#    - Use Unix `\n` line terminator
#    - sort header (fieldnames)
# 3. Run doctests - all must succeed

# Polish
# 1. Za pomocą `csv.DictWriter()` zapisz dane do `FILE`
# 2. Wymagania niefunkcjonalne:
#    - Użyj `,` do oddzielenia kolumn
#    - Użyj kodowania `utf-8`
#    - Użyj zakończenia linii Unix `\n`
#    - posortuj nagłówek (fieldnames)
# 3. Uruchom doctesty - wszystkie muszą się powieść

# region Show Hints
# - `vars()`
# - `sorted()`
# - `dict.keys()`
# - `csv.DictWriter()`
# endregion

# %% Your code
DATA = map(vars, DATA)
with open(FILE, mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['age', 'firstname', 'lastname'],
                            lineterminator='\n', quotechar='"',
                            quoting=csv.QUOTE_NONE)
    writer.writeheader()
    writer.writerows(DATA)
