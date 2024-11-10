

"""
* Assignment: Serialization Load FixedHeader
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Convert `DATA` to `result: list[dict]`
    2. Use `HEADER` as dict keys
    3. Do not convert numeric values to `float`, leave them as `str`
    4. Run doctests - all must succeed

Polish:
    1. Przekonwertuj `DATA` to `result: list[dict]`
    2. Użyj `HEADER` jako kluczy dictów
    3. Nie konwertuj wartości numerycznychh do `float`, pozostaw je jako `str`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.splitlines()`
    * `str.split()`
    * `list.append()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> result = list(result)  # expand map object
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is dict for x in result), \
    'All rows in `result` should be dict'

    >>> pprint(result)
    [{'petal_length': '5.1',
      'petal_width': '1.9',
      'sepal_length': '5.8',
      'sepal_width': '2.7',
      'species': 'virginica'},
     {'petal_length': '1.4',
      'petal_width': '0.2',
      'sepal_length': '5.1',
      'sepal_width': '3.5',
      'species': 'setosa'},
     {'petal_length': '4.1',
      'petal_width': '1.3',
      'sepal_length': '5.7',
      'sepal_width': '2.8',
      'species': 'versicolor'}]
"""

DATA = """5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor"""

HEADER = [
    'sepal_length',
    'sepal_width',
    'petal_length',
    'petal_width',
    'species',
]

# Replace keys with `HEADER`
# type: list[dict[str,str]]
result = ...

