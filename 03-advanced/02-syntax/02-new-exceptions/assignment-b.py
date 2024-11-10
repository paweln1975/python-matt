"""
* Assignment: Exception New Kelvin
* Type: homework
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Check value `value` passed to a `result` function
    2. If `value` is lower than 0, raise `NegativeKelvinError`
    3. Run doctests - all must succeed

Polish:
    1. Sprawdź wartość `value` przekazaną do funckji `result`
    2. Jeżeli `value` jest mniejsze niż 0, podnieś `NegativeKelvinError`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `raise`
    * `if`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> isclass(NegativeKelvinError)
    True
    >>> issubclass(NegativeKelvinError, Exception)
    True

    >>> result(1)
    >>> result(0)

    >>> try:
    ...     result(-1)
    ... except NegativeKelvinError:
    ...     True
    True
"""

class NegativeKelvinError(Exception):
    pass

# Check value `value` passed to a `result` function
# If `value` is lower than 0, raise `NegativeKelvinError`
# type: Callable[[int], NoReturn]
def result(value):
    ...


