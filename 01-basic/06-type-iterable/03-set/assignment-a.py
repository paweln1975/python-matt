"""
* Assignment: Iterable Set Create
* Type: class assignment
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Create sets:
        a. `result_a` without elements
        b. `result_b` with elements: 1, 2, 3
        c. `result_c` with elements: 1.1, 2.2, 3.3
        d. `result_d` with elements: 'a', 'b', 'c'
        e. `result_e` with elements: True, False, None
        f. `result_f` with elements: 1, 2.2, True, 'a'
    2. Run doctests - all must succeed

Polish:
    1. Stwórz sety:
        a. `result_a` bez elementów
        b. `result_b` z elementami: 1, 2, 3
        c. `result_c` z elementami: 1.1, 2.2, 3.3
        d. `result_d` z elementami: 'a', 'b', 'c'
        e. `result_e` z elementami: True, False, None
        f. `result_f` z elementami: 1, 2.2, True, 'a'
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

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

    >>> assert type(result_a) is set, \
    'Variable `result_a` has invalid type, should be set'
    >>> assert type(result_b) is set, \
    'Variable `result_b` has invalid type, should be set'
    >>> assert type(result_c) is set, \
    'Variable `result_c` has invalid type, should be set'
    >>> assert type(result_d) is set, \
    'Variable `result_d` has invalid type, should be set'
    >>> assert type(result_e) is set, \
    'Variable `result_e` has invalid type, should be set'
    >>> assert type(result_f) is set, \
    'Variable `result_f` has invalid type, should be set'

    >>> assert result_a == set(), \
    'Variable `result_a` has invalid value, should be set()'
    >>> assert result_b == {1, 2, 3}, \
    'Variable `result_b` has invalid value, should be {1, 2, 3}'
    >>> assert result_c == {1.1, 2.2, 3.3}, \
    'Variable `result_c` has invalid value, should be {1.1, 2.2, 3.3}'
    >>> assert result_d == {'a', 'b', 'c'}, \
    'Variable `result_d` has invalid value, should be {"a", "b", "c"}'
    >>> assert result_e == {True, False, None}, \
    'Variable `result_e` has invalid value, should be {True, False, None}'
    >>> assert result_f == {1, 2.2, True, 'a'}, \
    'Variable `result_f` has invalid value, should be {1, 2.2, True, "a"}'
"""

# Set without elements
# type: set
result_a = set()

# Set with elements: 1, 2, 3
# type: set[int]
result_b = {1, 2, 3}

# Set with elements: 1.1, 2.2, 3.3
# type: set[float]
result_c = {1.1, 2.2, 3.3}

# Set with elements:
# type: set[str]
result_d = {'a', 'b', 'c'}

# Set with elements: True, False, None
# type: set[bool|None]
result_e = {True, False, None}

# Set with elements: 1, 2.2, True, 'a'
# type: set[int|float|bool|str]
result_f = {1, 2.2, True, 'a'}

