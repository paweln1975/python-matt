
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> result = list(result)  # expand map object
>>> assert type(result) is list, \
'Variable `result` has invalid type, should be list'
>>> assert all(type(x) is tuple for x in result), \
'All rows in `result` should be tuple'

>>> from pprint import pprint
>>> pprint(result)
[('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
 (5.8, 2.7, 5.1, 1.9, 'virginica'),
 (5.1, 3.5, 1.4, 0.2, 'setosa'),
 (5.7, 2.8, 4.1, 1.3, 'versicolor')]
"""
# endregion

# region Show Types
result: list[tuple]
# endregion

DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor"""

# English
# 1. Convert `DATA` to `result: list[tuple[str]]`
# 2. Convert numeric values to `float`
# 3. Run doctests - all must succeed

# Polish
# 1. Przekonwertuj `DATA` to `result: list[tuple[str]]`
# 2. Przekonwertuj wartości numeryczne do `float`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# region Show Hints
# - `a, *b = ...`
# - `str.splitlines()`
# - `str.split()`
# - `dict.get()`
# - `float()`
# - `tuple()`
# - `tuple() + tuple()`
# - `list.append()`
# endregion

# %% Your code
header, *rows = DATA.splitlines()

result = []
header = tuple(header.split(','))
result.append(header)
for row in rows:
    *data, species = row.split(',')
    data = map(float, data)
    result.append(tuple(data) + (species,))
