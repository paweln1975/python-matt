"""
* Assignment: OOP ObjectConstructor Syntax
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Define class `Point` with methods:
        a. `__new__()` taking `x` and `y` and returns new class instance
        b. `__init__()` takes `x` and `y` and stores them as attributes
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Point` z metodami:
        a. `__new__()` przyjmuje  `x` i `y` i zwraca nową instancję klasy
        b. `__init__()` przyjmuje `x` i `y` i zapisuje je jako atrybuty
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Point)
    >>> assert hasattr(Point, '__new__')
    >>> assert hasattr(Point, '__init__')
    >>> pt = Point(1, 2)
    >>> assert type(pt) is Point
    >>> assert pt.x == 1
    >>> assert pt.y == 2
"""


# Define class `Point` with methods:
# - `__new__()` taking `x` and `y` and returns new class instance
# - `__init__()` taking `x` and `y` and stores them as attributes
# type: type
class Point:
    ...


