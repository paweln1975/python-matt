
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
>>> assert all(type(x) is dict for x in result), \
'All rows in `result` should be dict'

>>> from os import remove
>>> remove(FILE)

>>> from pprint import pprint
>>> pprint(result, sort_dicts=False)
[{'firstname': 'Mark', 'lastname': 'Watney', 'age': '42'},
 {'firstname': 'Melissa', 'lastname': 'Lewis', 'age': '41'},
 {'firstname': 'Rick', 'lastname': 'Martinez', 'age': '40'},
 {'firstname': 'Alex', 'lastname': 'Vogel', 'age': '42'},
 {'firstname': 'Beth', 'lastname': 'Johanssen', 'age': '29'},
 {'firstname': 'Chris', 'lastname': 'Beck', 'age': '36'}]
"""
# endregion

# region Show Imports
import csv
# endregion

# region Show Types
result: list[dict[str,str,int]]
# endregion

FILE = r'_temporary.csv'

DATA = """
firstname,lastname,age
Mark,Watney,42
Melissa,Lewis,41
Rick,Martinez,40
Alex,Vogel,42
Beth,Johanssen,29
Chris,Beck,36
"""

with open(FILE, mode='wt', encoding='utf-8') as file:
    file.write(DATA.lstrip())

# English
# 1. Define `result: list[dict]`
# 2. To `result` add data read from `FILE`
# 3. Use `csv.DictReader` to parse file
# 4. Do not convert values to `int`, leave as `str`
# 5. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result: list[dict]`
# 2. Do `result` dodaj wczytane dane z pliku `FILE`
# 3. Użyj `csv.DictReader` do sparsowania pliku
# 4. Nie konwertuj wartości na `int`, pozostaw jako `str`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code
result = []
with open(FILE, mode='rt', encoding='utf-8') as file:
    reader = csv.DictReader(file, fieldnames=['firstname', 'lastname', 'age'],
                            lineterminator='\n', quotechar='"',
                            quoting=csv.QUOTE_NONE)
    _ = next(reader)
    for x in reader:
        result.append(x)
