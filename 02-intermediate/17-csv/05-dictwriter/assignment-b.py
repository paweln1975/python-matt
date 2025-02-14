
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
"age","firstname","lastname"
"","Mark","Watney"
"41","Melissa",""
"","Rick","Martinez"
"42","","Vogel"
"29","Beth",""
"36","","Beck"
<BLANKLINE>
"""
# endregion

# region Show Imports
import csv
# endregion

FILE = r'_temporary.csv'

DATA = [
    {'firstname': 'Mark', 'lastname': 'Watney'},
    {'firstname': 'Melissa', 'age': 41},
    {'lastname': 'Martinez', 'firstname': 'Rick'},
    {'lastname': 'Vogel', 'age': 42},
    {'age': 29, 'firstname': 'Beth'},
    {'age': 36, 'lastname': 'Beck', },
]

# English
# 1. Using `csv.DictWriter()` write variable schema data to `FILE`
# 2. `fieldnames` must be automatically generated from `DATA`
# 3. Non functional requirements:
#    - All fields must be enclosed by double quote `"` character
#    - Use `,` to separate columns
#    - Use `utf-8` encoding
#    - Use Unix `\n` line terminator
#    - Sort `fieldnames` using `sorted()`
# 4. Run doctests - all must succeed

# Polish
# 1. Za pomocą `csv.DictWriter()` zapisz dane o zmiennej strukturze do `FILE`
# 2. `fieldnames` musi być generowane automatycznie na podstawie `DATA`
# 3. Wymagania niefunkcjonalne:
#    - Wszystkie pola muszą być otoczone znakiem cudzysłowu `"`
#    - Użyj `,` do oddzielenia kolumn
#    - Użyj kodowania `utf-8`
#    - Użyj zakończenia linii Unix `\n`
#    - Posortuj `fieldnames` używając `sorted()`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code

with open(FILE, mode='wt', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['age', 'firstname', 'lastname'],
                            lineterminator='\n', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(DATA)
