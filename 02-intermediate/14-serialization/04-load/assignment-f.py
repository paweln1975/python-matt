

"""
* Assignment: Serialization Load GenerateHeader
* Complexity: hard
* Lines of code: 7 lines
* Time: 8 min

English:
    1. Generate `header: list[str]` from first line `DATA`
    2. Convert `DATA` to `result: list[dict]`
    3. Use `header` as keys
    4. Convert numeric values to `float`
    5. Run doctests - all must succeed

Polish:
    1. Wygeneruj `header: list[str]` z pierwszej linii `DATA`
    2. Przekonwertuj `DATA` to `result: list[dict]`
    3. Użyj nagłówka jako kluczy
    4. Przekonwertuj wartości numeryczne do `float`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.split()`
    * `list() + list()`
    * `list.append()`
    * `tuple()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> result = list(result)
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is dict for x in result), \
    'All rows in `result` should be dict'

    >>> pprint(result)
    [{'petal_length': 5.1,
      'petal_width': 1.9,
      'sepal_length': 5.8,
      'sepal_width': 2.7,
      'species': 'virginica'},
     {'petal_length': 1.4,
      'petal_width': 0.2,
      'sepal_length': 5.1,
      'sepal_width': 3.5,
      'species': 'setosa'},
     {'petal_length': 4.1,
      'petal_width': 1.3,
      'sepal_length': 5.7,
      'sepal_width': 2.8,
      'species': 'versicolor'}]
"""

DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor"""

# replace fieldnames with `FIELDNAMES`
# type: list[dict]
result = ...

