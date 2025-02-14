
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

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
# endregion

# region Show Types
Point: type
Path: type
# endregion

# English
# 1. Define class `Point` with:
#    - attribute `x: int`
#    - attribute `y: int`
#    - method `__repr__()` returning f'Point(x={self.x}, y={self.y})'
# 2. Define class `Path` with attributes:
#    - `points: list[Point]` with default empty list
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasę `Point` z:
#    - atrybut `x: int`
#    - atrybut `y: int`
#    - metodą `__repr__()` zwracającą f'Point(x={self.x}, y={self.y})'
# 2. Zdefiniuj klasę `Path` z atrybutami:
#    - `points: list[Point]` z domyślną pustą listą
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

class Path:
    def __init__(self, points = None):
        self.points = points if points is not None else []
