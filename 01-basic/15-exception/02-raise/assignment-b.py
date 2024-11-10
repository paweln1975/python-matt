"""
* Assignment: Exception Raise Many
* Type: class assignment
* Complexity: easy
* Lines of code: 6 lines
* Time: 3 min

English:
    1. Validate value passed to a `result` function
    2. If `value` is:
        a. other type than `int` or `float` raise `TypeError`
        b. less than zero, raise `ValueError`
        c. below `ADULT`, raise `PermissionError`
    3. Write solution inside `result` function
    4. Run doctests - all must succeed

Polish:
    1. Sprawdź poprawność wartości przekazanej do funckji `result`
    2. Jeżeli `age` jest:
        a. innego typu niż `int` lub `float`, podnieś wyjątek `TypeError`
        b. mniejsze niż zero, podnieś wyjątek `ValueError`
        c. mniejsze niż `ADULT`, podnieś wyjątek `PermissionError`
    3. Rozwiązanie zapisz wewnątrz funkcji `result`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `not in`
    * `raise`
    * `if`
    * `isinstance()`
    * `type()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result(18)
    >>> result(17.9999)
    Traceback (most recent call last):
    PermissionError
    >>> result(-1)
    Traceback (most recent call last):
    ValueError
    >>> result('one')
    Traceback (most recent call last):
    TypeError
    >>> result(True)
    Traceback (most recent call last):
    TypeError
"""

ADULT = 18

# Validate value passed to a `result` function
# If `value` is:
#  a. other type than `int` or `float` raise `TypeError`
#  b. less than zero, raise `ValueError`
#  c. below `ADULT`, raise `PermissionError`
# Write solution inside `result` function
# type: Callable[[int|float], None]
def result(age):
    if type(age) not in [float, int]:
        raise TypeError
    elif age < 0:
        raise ValueError
    elif age < 18:
        raise PermissionError


