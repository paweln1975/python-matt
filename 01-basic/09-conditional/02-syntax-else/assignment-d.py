"""
* Assignment: Conditional If Segmentation
* Type: class assignment
* Complexity: easy
* Lines of code: 6 lines
* Time: 3 min

English:
    1. If variable DIGIT is in range:
        a. from 0 to 3 (exclusive) - then increment variable `result['small']` by 1
        b. from 3 to 7 (exclusive) - then increment variable `result['medium']` by 1
        c. from 7 to 10 (exclusive) - then increment variable `result['large']` by 1
    3. Run doctests - all must succeed

Polish:
    1. Jeżeli zmienna DIGIT jest w zakresie:
        a. od 0 do 3 (rozłącznie) - wtedy zwiększ zmienną `result['small']` o 1
        b. od 3 do 7 (rozłącznie) - wtedy zwiększ zmienną `result['medium']` o 1
        c. od 7 do 10 (rozłącznie) - wtedy zwiększ zmienną `result['large']` o 1
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is dict, \
    'Variable `red` has invalid type, should be int'

    >>> assert all(type(x) is str for x in result.keys()), \
    'All dict keys should be str'
    >>> assert all(type(x) is int for x in result.values()), \
    'All dict keys should be int'

    >>> result = {'small': 0, 'medium': 1, 'large': 0}
"""

DIGIT = 5

result = {
    'small': 0,
    'medium': 0,
    'large': 0,
}

# If variable DIGIT is in range:
# - from 0 to 3 (exclusive) - then increment variable `result['small']` by 1
# - from 3 to 7 (exclusive) - then increment variable `result['medium']` by 1
# - from 7 to 10 (exclusive) - then increment variable `result['large']` by 1
# type: dict[str, int]
if 0 < DIGIT < 5:
    result['small'] += 1
if 3 < DIGIT < 7:
    result['medium'] += 1
if 7 < DIGIT < 10:
    result['large'] += 1



