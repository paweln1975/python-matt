"""
* Assignment: Iterator Enumerate ZeroPadded
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Convert `MONTH` into dict:
        a. key: str - month number
        b. value: str - month name
    2. Use enumerate() starting with 1
    3. Month number must be two letter string
       (zero padded) - np. 01, 02, ..., 09, 10, 11, 12
    4. Run doctests - all must succeed

Polish:
    1. Przekonwertuj `MONTH` w słownik:
        a. klucz: str - numer miesiąca
        b. wartość: str - nazwa miesiąca
    2. Użyj enumerate() zaczynając od 1
    3. Numer miesiąca ma być dwuznakowym stringiem
       (dopełnionym zerem) - np. 01, 02, ..., 09, 10, 11, 12
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * dict comprehension
    * `enumerate()`
    * `str.zfill()`
    * `f'{number:02}'`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'dict'>
    >>> '00' not in result
    True
    >>> '13' not in result
    True
    >>> result['01'] == 'January'
    True

    >>> assert all(type(x) is str for x in result.keys())
    >>> assert all(type(x) is str for x in result.values())
    >>> assert all(len(x) == 2 for x in result.keys())

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'01': 'January',
     '02': 'February',
     '03': 'March',
     '04': 'April',
     '05': 'May',
     '06': 'June',
     '07': 'July',
     '08': 'August',
     '09': 'September',
     '10': 'October',
     '11': 'November',
     '12': 'December'}
"""

MONTHS = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']

# With zero-padded number and month name
# type: dict[str,str]
result = ...

