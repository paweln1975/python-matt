"""
* Assignment: Exception Catch Else
* Type: class assignment
* Complexity: easy
* Lines of code: 7 lines
* Time: 3 min

English:
    1. Convert value passed to the `result` function as a `float`
    2. If conversion fails, raise `TypeError`
    3. If value is below ADULT, raise `PermissionError`
    4. Write solution inside `result` function
    5. Run doctests - all must succeed

Polish:
    1. Przekonwertuj wartośc przekazaną do funckji `result` jako `float`
    2. Jeżeli konwersja się nie powiedzie, podnieś `TypeError`
    3. Jeżeli wartość jest poniżej ADULT, podnieś `PermissionError`
    4. Rozwiązanie zapisz wewnątrz funkcji `result`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `try`
    * `except`
    * `else`
    * `raise`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result(21)
    >>> result('one')
    Traceback (most recent call last):
    TypeError
    >>> result(1)
    Traceback (most recent call last):
    PermissionError
"""

ADULT = 18

# Przekonwertuj wartośc przekazaną do funckji `result` jako `float`
# Jeżeli konwersja się nie powiedzie, podnieś `TypeError`
# Jeżeli wartość jest poniżej ADULT, podnieś `PermissionError`
# Rozwiązanie zapisz wewnątrz funkcji `result`
# type: Callable[[int|float], None]
def result(age):
    try:
        float(age)
    except:
        raise TypeError
    else:
        if age < ADULT:
            raise PermissionError


