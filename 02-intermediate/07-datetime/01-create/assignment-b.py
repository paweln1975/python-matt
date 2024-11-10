"""
* Assignment: Datetime Create Attributes
* Complexity: easy
* Lines of code: 7 lines
* Time: 3 min

English:
    1. Use `DATA: datetime`
    2. Define variables:
        a. `result_a: int` with year from `DATA`
        b. `result_b: int` with month from `DATA`
        c. `result_c: int` with day from `DATA`
        d. `result_d: int` with hour from `DATA`
        e. `result_e: int` with minute from `DATA`
        f. `result_f: int` with second from `DATA`
        g. `result_g: int` with microsecond from `DATA`
    3. Run doctests - all must succeed

Polish:
    1. Użyj `DATA: datetime`
    2. Zdefiniuj zmienne:
        a. `result_a: int` z rokiem z `DATA`
        b. `result_b: int` z miesiącem z `DATA`
        c. `result_c: int` z dniem z `DATA`
        d. `result_d: int` z godziną z `DATA`
        e. `result_e: int` z minutą z `DATA`
        f. `result_f: int` z sekundą z `DATA`
        g. `result_g: int` z mikrosekundą z `DATA`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result_a is not Ellipsis, \
    'Assign result to variable: `result_a`'
    >>> assert type(result_a) is int, \
    'Variable `result_a` has invalid type, must be an int'
    >>> result_a
    1969

    >>> assert result_b is not Ellipsis, \
    'Assign result to variable: `result_b`'
    >>> assert type(result_b) is int, \
    'Variable `result_b` has invalid type, must be an int'
    >>> result_b
    7

    >>> assert result_c is not Ellipsis, \
    'Assign result to variable: `result_c`'
    >>> assert type(result_c) is int, \
    'Variable `result_c` has invalid type, must be an int'
    >>> result_c
    21

    >>> assert result_d is not Ellipsis, \
    'Assign result to variable: `result_d`'
    >>> assert type(result_d) is int, \
    'Variable `result_d` has invalid type, must be an int'
    >>> result_d
    2

    >>> assert result_e is not Ellipsis, \
    'Assign result to variable: `result_e`'
    >>> assert type(result_e) is int, \
    'Variable `result_e` has invalid type, must be an int'
    >>> result_e
    56

    >>> assert result_f is not Ellipsis, \
    'Assign result to variable: `result_f`'
    >>> assert type(result_f) is int, \
    'Variable `result_f` has invalid type, must be an int'
    >>> result_f
    15

    >>> assert result_g is not Ellipsis, \
    'Assign result to variable: `result_g`'
    >>> assert type(result_g) is int, \
    'Variable `result_g` has invalid type, must be an int'
    >>> result_g
    0
"""

from datetime import datetime


DATA = datetime(1969, 7, 21, 2, 56, 15)


# year from `DATA`
# type: int
result_a = ...

# month from `DATA`
# type: int
result_b = ...

# day from `DATA`
# type: int
result_c = ...

# hour from `DATA`
# type: int
result_d = ...

# minute from `DATA`
# type: int
result_e = ...

# second from `DATA`
# type: int
result_f = ...

# microsecond from `DATA`
# type: int
result_g = ...

