"""
* Assignment: Type Str Normalize
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Use `str` methods to clean `DATA`
    2. Run doctests - all must succeed

Polish:
    1. Wykorzystaj metody `str` do oczyszczenia `DATA`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> pprint(result)
    'Pana Twardowskiego III'
"""

DATA = 'UL. pana \tTWArdoWskIEGO 3'

# Expected result: 'Pana Twardowskiego III'
# type: str
result = (DATA.removeprefix('UL. ').replace('\t', '')
          .title().replace('3','III'))

