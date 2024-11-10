"""
* Assignment: Loop Unpack Between
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Use `DATA: list[tuple]` variable
    2. Define `result: list[tuple]` with first names and last names
       of people whose age is in the range 18 to 65
    3. Use unpack syntax in a for loop
    5. Run doctests - all must succeed

Polish:
    1. Użyj zmiennej `DATA: list[tuple]`
    2. Zdefiniuj `result: list[tuple]` imionami i nazwiskami osób,
       których wiek jest w przedziale 18 do 65 lat
    3. Użyj składni rozpakowania w pętli for
    5. Uruchom doctesty - wszystkie muszą się powieść

Why:
    * Check if you can filter data
    * Check if you know string methods
    * Check if you know how to iterate over list[dict]

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Result must be a list'
    >>> assert len(result) > 0, \
    'Result cannot be empty'
    >>> assert all(type(element) is tuple for element in result), \
    'All elements in result must be a tuple'

    >>> pprint(result)
    [('Mark', 'Watney'),
     ('Melissa', 'Lewis'),
     ('Rick', 'Martinez'),
     ('Alex', 'Vogel'),
     ('Chris', 'Beck'),
     ('Beth', 'Johanssen')]
"""

DATA = [
    ('Mark', 'Watney', 41),
    ('Melissa', 'Lewis', 40),
    ('Rick', 'Martinez', 39),
    ('Alex', 'Vogel', 40),
    ('Chris', 'Beck', 36),
    ('Beth', 'Johanssen', 29),
    ('Pan', 'Twardowski', 529),
    ('Ivan', 'Ivanovich', 1),
]

# Define `result: list[tuple]` with first names and last names
# of people whose age is in the range 18 to 65
# Use unpack syntax in a for loop
# type: list[str]

result = []
for firstname, lastname, age in DATA:
    if 18 < age < 65:
        result.append((firstname, lastname))


