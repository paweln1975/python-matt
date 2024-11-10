"""
* Assignment: OOP Property Getter
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define property `position` in class `Point`
    2. Accessing `position` returns tuple `(x, y, z)`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj property `position` w klasie `Point`
    2. Dostęp do `position` zwraca tuplę `(x, y, z)`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pt = Point(x=1, y=2, z=3)
    >>> pt.x, pt.y, pt.z
    (1, 2, 3)
    >>> pt.position
    (1, 2, 3)
"""

# Define property `position` in class `Point`
# Accessing `position` returns tuple `(x, y, z)`
# type: type[Point]
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


