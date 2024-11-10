"""
* Assignment: Comprehension Nested Dict
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 5 min

English:
    1. Convert to `result: dict[str,int]`
    2. Use nested dict comprehension
    3. Run doctests - all must succeed

Polish:
    1. Przekonwertuj do `result: dict[str,int]`
    2. Użyj zagnieżdżonego rozwinięcia słownikowego
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * nested `for`
    * `dict.items()`
    * `str()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> type(result)
    <class 'dict'>

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

# Converted DATA
# type: dict[str,int]
result = {name:key
          for key, names in DATA.items()
          for name in names}



