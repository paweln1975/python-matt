"""
* Assignment: Star Parameters Args
* Complexity: easy
* Lines of code: 6 lines
* Time: 8 min

English:
    1. Define function `isnumeric()`
        a. Function takes arbitrary number of positional arguments
        b. Arguments can be of any type
        c. Return `True` if all arguments are `int` or `float` only
        d. Return `False` if any argument is different type
    2. Compare using `type()` and `isinstance()`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `isnumeric()`
        a. Funkcja przyjmuje dowolną liczbę argumentów pozycyjnych
        b. Podawane argumenty mogą być dowolnego typu
        c. Zwróć `True` jeżeli wszystkie argumenty są tylko typów `int` lub `float`
        d. Zwróć `False` jeżeli którykolwiek jest innego typu
    2. Porównaj użycie `type()` i `isinstance()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `isinstance(obj, type1|type2)`
    * `type(obj)`
    * `... in tuple()``
    * `raise TypeError('error message')`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(isnumeric), \
    'isnumeric must be a function'

    >>> isnumeric()
    Traceback (most recent call last):
    TypeError: At least one argument is required

    >>> isnumeric(1)
    True
    >>> isnumeric(1.0)
    True
    >>> isnumeric('one')
    False
    >>> isnumeric(True)
    False

    >>> isnumeric(1, 1.0)
    True
    >>> isnumeric(1,  1.0, 'one')
    False
"""


# Return True if all arguments are int or float, otherwise False
# type: Callable[[int|float],bool]
def isnumeric(*args):
    ...


