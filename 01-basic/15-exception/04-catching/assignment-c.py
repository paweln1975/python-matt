"""
* Assignment: Exception Catch Finally
* Type: class assignment
* Complexity: easy
* Lines of code: 8 lines
* Time: 3 min

English:
    1. Convert value passed to the function as a `degrees: int`
    2. If conversion fails, raise exception `TypeError` with message:
       'Invalid type, expected int or float'
    3. Use `finally` to print `degrees` value
    4. Write solution inside `result` function
    5. Run doctests - all must succeed

Polish:
    1. Przekonwertuj wartość przekazaną do funckji jako `degrees: int`
    2. Jeżeli konwersja się nie powiedzie to podnieś wyjątek `TypeError`
       z komunikatem 'Invalid type, expected int or float'
    3. Użyj `finally` do wypisania wartości `degrees`
    4. Rozwiązanie zapisz wewnątrz funkcji `result`
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `try`
    * `except`
    * `finally`
    * `raise`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result(1)
    1
    >>> result(180)
    180
    >>> result(1.0)
    1
    >>> result('one')
    Traceback (most recent call last):
    TypeError: Invalid type, expected int or float
"""

# Convert value passed to the function as a `degrees: int`
# If conversion fails, raise exception `TypeError` with message:
# 'Invalid type, expected int or float'
# Use `finally` to print `degrees` value
# Write solution inside `result` function
# type: Callable[[int], None]
def result(degrees):
    try:
        degrees = int(degrees)
    except ValueError:
        raise TypeError('Invalid type, expected int or float')
    finally:
        print(degrees)


