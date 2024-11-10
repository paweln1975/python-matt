"""
* Assignment: Loop Dict To Dict
* Type: class assignment
* Complexity: medium
* Lines of code: 3 lines
* Time: 8 min

English:
    1. Convert to `result: dict[str, int]`
    2. Run doctests - all must succeed

Polish:
    1. Przekonwertuj do `result: dict[str, int]`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'

    >>> pprint(result, sort_dicts=False)
    {'Doctorate': 6,
     'Prof-school': 6,
     'Masters': 5,
     'Bachelor': 5,
     'Engineer': 5,
     'HS-grad': 4,
     'Junior High': 3,
     'Primary School': 2,
     'Kindergarten': 1}
"""

DATA = {
    6: ['Doctorate', 'Prof-school'],
    5: ['Masters', 'Bachelor', 'Engineer'],
    4: ['HS-grad'],
    3: ['Junior High'],
    2: ['Primary School'],
    1: ['Kindergarten'],
}

# Converted DATA. Note values are str not int!
# type: dict[str,int]

result = {}
for key, names in DATA.items():
    for name in names:
        result[name] = key

