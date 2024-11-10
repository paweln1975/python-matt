"""
* Assignment: Exception Catch Except
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Convert value passed to the `result` function as a `float`
    2. If conversion fails then print 'Invalid value'
    3. Write solution inside `result` function
    4. Run doctests - all must succeed

Polish:
    1. Przekonwertuj wartośc przekazaną do funckji `result` jako `float`
    2. Jeżeli konwersja się nie powiedzie to wypisz 'Invalid value'
    3. Rozwiązanie zapisz wewnątrz funkcji `result`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `try`
    * `except`
    * `print()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result('1')
    >>> result('1.0')
    >>> result('1,0')
    Invalid value
"""

# Convert value passed to the `result` function as a `float`
# If conversion fails then print 'Invalid value'
# Write solution inside `result` function
# type: Callable[[str], None]
def result(value):
    try:
        v = float(value)
    except ValueError:
        print('Invalid value')


