

"""
* Assignment: Serialization Load Encoder
* Complexity: medium
* Lines of code: 10 lines
* Time: 13 min

English:
    1. Convert `DATA` to `result: list[tuple[str]]`
    2. Generate `ENCODER: dict[int,str]` from `header: list[str]`
    3. Substitute last element (label) with value from `ENCODER`
    4. Run doctests - all must succeed

Polish:
    1. Przekonwertuj `DATA` to `result: list[tuple[str]]`
    2. Wygeneruj `ENCODER: dict[int,str]` z `header: list[str]`
    3. Podmień ostatni element (etykietę) z wartością z `ENCODER`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `a, *b = ...`
    * `dict(enumerate())`
    * `str.splitlines()`
    * `str.split()`
    * `dict.get()`
    * `int()`
    * `tuple()`
    * `tuple() + tuple()`
    * `list.append()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> result = list(result)  # expand map object
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is tuple for x in result), \
    'All rows in `result` should be tuple'

    >>> pprint(result)
    [('5.8', '2.7', '5.1', '1.9', 'virginica'),
     ('5.1', '3.5', '1.4', '0.2', 'setosa'),
     ('5.7', '2.8', '4.1', '1.3', 'versicolor')]
"""

DATA = """3,4,setosa,virginica,versicolor
5.8,2.7,5.1,1.9,1
5.1,3.5,1.4,0.2,0
5.7,2.8,4.1,1.3,2"""

# values from file (note the list[tuple] format!)
# type: list[tuple]
result = ...

