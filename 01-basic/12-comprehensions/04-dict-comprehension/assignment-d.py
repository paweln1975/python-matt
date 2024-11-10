"""
* Assignment: Comprehension Dict ZeroPadded
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: dict` with `DATA` converted into:
        a. Keys: month number
        b. Values: month name
    2. Month number must be two letter string (zero padded)
    3. Use dict comprehension
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: dict` z `DATA` przekonwertowanym w:
        a. klucz: numer miesiąca
        b. wartość: nazwa miesiąca
    2. Numer miesiąca ma być dwuznakowym stringiem (wypełnij zerem)
    3. Użyj rozwinięcia słownikowego
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `f'{number:02}'`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

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

    >>> pprint(result)
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

DATA = [
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'December'),
]

# Define `result: dict` with `DATA` converted into:
#  a. Keys: month number
#  b. Values: month name
# Month number must be two letter string (zero padded)
# Use dict comprehension
# type: dict[str,str]
result = {f'{idx:02}': month for idx, month in DATA}

country_code = '48'
print(f'{country_code:04}')
