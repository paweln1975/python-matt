"""
* Assignment: OOP Relations Association
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Define class `Point` with:
        a. attribute `x: int`
        b. attribute `y: int`
        c. method `__repr__()` returning f'Point(x={self.x}, y={self.y})'
    2. Define class `Path` with attributes:
        a. `points: list[Point]` with default empty list
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Point` z:
        a. atrybut `x: int`
        b. atrybut `y: int`
        c. metodą `__repr__()` zwracającą f'Point(x={self.x}, y={self.y})'
    2. Zdefiniuj klasę `Path` z atrybutami:
        a. `points: list[Point]` z domyślną pustą listą
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Point)
    >>> assert isclass(Path)

    >>> pt = Point(1, 2)
    >>> pt.x
    1
    >>> pt.y
    2
    >>> pt
    Point(x=1, y=2)

    >>> path = Path([
    ...     Point(x=1, y=2),
    ...     Point(x=3, y=4),
    ...     Point(x=5, y=6)]
    ... )

    >>> path.points
    [Point(x=1, y=2), Point(x=3, y=4), Point(x=5, y=6)]
"""

