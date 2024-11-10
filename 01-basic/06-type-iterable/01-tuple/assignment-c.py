"""
* Assignment: Iterable List Count
* Type: class assignment
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Count number of occurrences of value 1 in:
        a. `result_a` - number of occurrences in DATA_A
        b. `result_b` - number of occurrences in DATA_B
        c. `result_c` - number of occurrences in DATA_C
        d. `result_d` - number of occurrences in DATA_D
        e. `result_e` - number of occurrences in DATA_E
        f. `result_f` - number of occurrences in DATA_F
    2. Run doctests - all must succeed

Polish:
    1. Zlicz liczbę wystąpień wartości 1 w:
        a. `result_a` - liczba wystąpień w DATA_A
        b. `result_b` - liczba wystąpień w DATA_B
        c. `result_c` - liczba wystąpień w DATA_C
        d. `result_d` - liczba wystąpień w DATA_D
        e. `result_e` - liczba wystąpień w DATA_E
        f. `result_f` - liczba wystąpień w DATA_F
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result_a is not Ellipsis, \
    'Assign your result to variable `result_a`'
    >>> assert result_b is not Ellipsis, \
    'Assign your result to variable `result_b`'
    >>> assert result_c is not Ellipsis, \
    'Assign your result to variable `result_c`'
    >>> assert result_d is not Ellipsis, \
    'Assign your result to variable `result_d`'
    >>> assert result_e is not Ellipsis, \
    'Assign your result to variable `result_e`'
    >>> assert result_f is not Ellipsis, \
    'Assign your result to variable `result_f`'

    >>> assert type(result_a) is int, \
    'Variable `result_a` has invalid type, should be int'
    >>> assert type(result_b) is int, \
    'Variable `result_b` has invalid type, should be int'
    >>> assert type(result_c) is int, \
    'Variable `result_c` has invalid type, should be int'
    >>> assert type(result_d) is int, \
    'Variable `result_d` has invalid type, should be int'
    >>> assert type(result_e) is int, \
    'Variable `result_e` has invalid type, should be int'
    >>> assert type(result_f) is int, \
    'Variable `result_f` has invalid type, should be int'

    >>> assert result_a == 0, \
    'Variable `result_a` has invalid value. Check your calculations.'
    >>> assert result_b == 1, \
    'Variable `result_b` has invalid value. Check your calculations.'
    >>> assert result_c == 1, \
    'Variable `result_c` has invalid value. Check your calculations.'
    >>> assert result_d == 0, \
    'Variable `result_d` has invalid value. Check your calculations.'
    >>> assert result_e == 1, \
    'Variable `result_e` has invalid value. Check your calculations.'
    >>> assert result_f == 3, \
    'Variable `result_f` has invalid value. Check your calculations.'

    >>> pprint(result_a)
    0
    >>> pprint(result_b)
    1
    >>> pprint(result_c)
    1
    >>> pprint(result_d)
    0
    >>> pprint(result_e)
    1
    >>> pprint(result_f)
    3
"""

DATA_A = ()
DATA_B = (1, 2, 3)
DATA_C = (1.0, 2.0, 3.0)
DATA_D = ('1', '2', '3')
DATA_E = (True, False)
DATA_F = (1, 1.0, True, '1')

# Number of occurrences of value 1 in DATA_A
# type: int
result_a = DATA_A.count(1)

# Number of occurrences of value 1 in DATA_B
# type: int
result_b = DATA_B.count(1)

# Number of occurrences of value 1 in DATA_C
# type: int
result_c = DATA_C.count(1)

# Number of occurrences of value 1 in DATA_D
# type: int
result_d = DATA_D.count(1)

# Number of occurrences of value 1 in DATA_E
# type: int
result_e = DATA_E.count(1)

# Number of occurrences of value 1 in DATA_F
# type: int
result_f = DATA_F.count(1)

