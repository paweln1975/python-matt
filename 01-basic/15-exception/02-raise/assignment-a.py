"""
* Assignment: Exception Raise One
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Validate value passed to a `result` function:
        a. If `value` is less than zero, raise `ValueError`
    2. Write solution inside `result` function
    3. Run doctests - all must succeed

Polish:
    1. Sprawdź poprawność wartości przekazanej do funckji `result`:
        a. Jeżeli `value` jest mniejsze niż zero, podnieś wyjątek `ValueError`
    2. Rozwiązanie zapisz wewnątrz funkcji `result`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `if`
    * `raise`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result(1)
    >>> result(0)
    >>> result(-1)
    Traceback (most recent call last):
    ValueError
"""

# Validate value passed to a `result` function:
# If `value` is less than zero, raise `ValueError`
# Write solution inside `result` function
# type: Callable[[int], None]
def result(value):
    if value < 0:
        raise ValueError


