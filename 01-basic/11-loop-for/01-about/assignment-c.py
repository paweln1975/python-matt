"""
* Assignment: Loop For Segmentation
* Type: class assignment
* Complexity: easy
* Lines of code: 10 lines
* Time: 8 min

English:
    1. Count number of occurrences for digit in segments:
        a. 'small' - digitst in range [0-3)
        b. 'medium' - digitst in range [3-7)
        c. 'large' - digitst in range [7-10)
    2. Notation `[0-3)` - means, digits between 0 and 3, without 3 (left-side closed)
    3. Run doctests - all must succeed

Polish:
    1. Policz liczbę wystąpień cyfr w przedziałach:
        a. 'small' - cyfry z przedziału <0-3)
        b. 'medium' - cyfry z przedziału <3-7)
        c. 'large' - cyfry z przedziału <7-10)
    2. Zapis `<0-3)` - znaczy, cyfry od 0 do 3, bez 3 (lewostronnie domknięty)
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'

    >>> assert all(type(x) is str for x in result.keys())
    >>> assert all(type(x) is int for x in result.values())

    >>> result
    {'small': 16, 'medium': 19, 'large': 15}
"""

DATA = [
    1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
    0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
    2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
    1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
    4, 8, 1, 9, 6, 3,
]

# Number of digit occurrences in segments
# type: dict[str,int]
result = {'small': 0, 'medium': 0, 'large': 0}

for digit in DATA:
    if 0 <= digit < 3:
        result['small'] += 1
    if 3 <= digit < 7:
        result['medium'] += 1
    if 7 <= digit < 10:
        result['large'] += 1
