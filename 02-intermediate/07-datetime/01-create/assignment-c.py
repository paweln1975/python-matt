"""
* Assignment: Datetime Create Split
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. First human (Yuri Gagarin) flown to space on
       April 12th, 1961 at 6:07 a.m. from Bajkonur Cosmodrome in Kazahstan
    2. Use `DATE: datetime`
    3. Define variables:
        a. `result_a: date` to represent date of the launch
        b. `result_b: time` to represent time of the launch
    4. Run doctests - all must succeed

Polish:
    1. Pierwszy człowiek (Juri Gagarin) poleciał w kosmos
       12 kwietnia 1961 roku o 6:07 rano z kosmodromu Bajkonur w Kazachstanie
    2. Użyj `DATE: datetime`
    3. Zdefiniuj zmienne:
        a. `result_a: date` do reprezentacji datę startu
        b. `result_b: time` do reprezentacji czas startu
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result_a is not Ellipsis, \
    'Assign result to variable: `result_a`'
    >>> assert type(result_a) is date, \
    'Variable `result_a` has invalid type, must be a date'
    >>> print(result_a)
    1961-04-12

    >>> assert result_b is not Ellipsis, \
    'Assign result to variable: `result_b`'
    >>> assert type(result_b) is time, \
    'Variable `result_b` has invalid type, must be a time'
    >>> print(result_b)
    06:07:00
"""

from datetime import date, datetime, time


DATA = datetime(1961, 4, 12, 6, 7)

# date of the launch
# type: date
result_a = ...

# time of the launch
# type: time
result_b = ...


