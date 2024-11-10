"""
* Assignment: Accessor Property NonNegative
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Define class `Point` with:
        a. Attribute `x: int`
        b. Attribute `y: int`
        c. Attribute `z: int`
        d. Property `position`
    3. Setting `position` raises ValueError
       if any value is less than 0
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Point` z:
        a. Atrybut `x: int`
        b. Atrybut `y: int`
        c. Atrybut `z: int`
        d. Property `position`
    3. Ustawianie `position` podnosi wyjątek,
       jeżeli którakolwiek wartość jest mniejsza od 0
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pt = Point()

    >>> pt.position = 1, 2, 3
    >>> assert pt.x == 1
    >>> assert pt.y == 2
    >>> assert pt.z == 3

    >>> pt.position = -1, 2, 3
    Traceback (most recent call last):
    ValueError

    >>> pt.position = 1, -2, 3
    Traceback (most recent call last):
    ValueError

    >>> pt.position = 1, 2, -3
    Traceback (most recent call last):
    ValueError
"""


# Define class `Point` with:
# - Attribute `x: int`
# - Attribute `y: int`
# - Attribute `z: int`
# - Property `position`
# Setting `position` raises ValueError
# if any value is less than 0
# type: type[Point]
class Point:
    x: int
    y: int
    z: int


