
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
"firstname","groups","lastname"
"Mark","1,users","Watney"
"Melissa","1,users;2,admins","Lewis"
"Rick","","Martinez"
<BLANKLINE>
"""
# endregion

# region Show Imports
import csv
# endregion

FILE = r'_temporary.csv'

class Group:
    gid: int
    name: str

    def __init__(self, gid, name):
        self.gid = gid
        self.name = name

class User:
    firstname: str
    lastname: str
    groups: list[Group]

    def __init__(self, firstname, lastname, groups=None):
        self.firstname = firstname
        self.lastname = lastname
        self.groups = list(groups) if groups else []

DATA = [
    User('Mark', 'Watney', groups=[
        Group(gid=1, name='users')]),
    User('Melissa', 'Lewis', groups=[
        Group(gid=1, name='users'),
        Group(gid=2, name='admins')]),
    User('Rick', 'Martinez', groups=[]),
]

# English
# 1. Using `csv.DictWriter()` save `DATA` to `FILE`
# 2. Non-functional requirements:
#    - All fields must be enclosed by double quote `"` character
#    - Use `,` to separate mission fields
#    - Use `;` to separate missions
#    - Use Unix `\n` newline
#    - Sort `fieldnames` using `sorted()`
# 3. Run doctests - all must succeed

# Polish
# 1. Za pomocą `csv.DictWriter()` zapisz `DATA` do `FILE`
# 2. Wymagania niefunkcjonalne:
#    - Wszystkie pola muszą być otoczone znakiem cudzysłowu `"`
#    - Użyj `,` do oddzielania pól mission
#    - Użyj `;` do oddzielenia missions
#    - Użyj zakończenia linii Unix `\n`
#    - Posortuj `fieldnames` używając `sorted()`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# region Show Hints
# - `vars(obj)`
# - Nested `for`
# - `str.join(';', sequence)`
# - `str.join(',', sequence)`
# endregion

# %% Your code

result = []
for user in DATA:
    firstname = user.firstname
    lastname = user.lastname
    groups = []
    for group in user.groups:
        gid = group.gid
        name = group.name
        groups.append(f'{gid},{name}')
    result.append(
        {'firstname': firstname,
         "groups": ';'.join(groups),
         'lastname': lastname})


header = "firstname","groups","lastname"

with open(FILE, mode='wt', encoding='utf-8') as file:
    writer = csv.DictWriter(file,
                            fieldnames=header,
                            lineterminator='\n',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(result)
