
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass, ismethod
>>> assert isclass(Point)
>>> assert isclass(Position)
>>> assert hasattr(Position, 'get_position')
>>> assert hasattr(Position, 'set_position')
>>> assert hasattr(Position, 'change_position')
>>> assert ismethod(Position().get_position)
>>> assert ismethod(Position().set_position)
>>> assert ismethod(Position().change_position)

>>> class User(Position):
...     pass

>>> mark = User()

>>> mark.set_position(x=1, y=2)
>>> mark.get_position()
Point(x=1, y=2)

>>> mark.set_position(x=1, y=1)
>>> mark.change_position(right=1)
>>> mark.get_position()
Point(x=2, y=1)

>>> mark.set_position(x=1, y=1)
>>> mark.change_position(left=1)
>>> mark.get_position()
Point(x=0, y=1)

>>> mark.set_position(x=1, y=1)
>>> mark.change_position(down=1)
>>> mark.get_position()
Point(x=1, y=2)

>>> mark.set_position(x=1, y=1)
>>> mark.change_position(up=1)
>>> mark.get_position()
Point(x=1, y=0)
"""
# endregion

# region Show Types
from typing import Callable
Point: type
Position: type
get_position: Callable[[object], object]
set_position: Callable[[object, int, int], None]
change_position: Callable[[object, int, int, int, int], None]
# endregion

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

# English
# 1. Define class `Point`
# 2. Class `Point` has attributes `x: int = 0` and `y: int = 0`
# 3. Define class `Position`
# 4. In `Position` define method `get_position(self) -> Point`
# 5. In `Position` define method `set_position(self, x: int, y: int) -> None`
# 6. In `Position` define method `change_position(self, left: int = 0, right: int = 0, up: int = 0, down: int = 0) -> None`
# 7. Assume left-top screen corner as an initial coordinates position:
#    - going right add to `x`
#    - going left subtract from `x`
#    - going up subtract from `y`
#    - going down add to `y`
# 8. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasę `Point`
# 2. Klasa `Point` ma atrybuty `x: int = 0` oraz `y: int = 0`
# 3. Zdefiniuj klasę `Position`
# 4. W `Position` zdefiniuj metodę `get_position(self) -> Point`
# 5. W `Position` zdefiniuj metodę `set_position(self, x: int, y: int) -> None`
# 6. W `Position` zdefiniuj metodę `change_position(self, left: int = 0, right: int = 0, up: int = 0, down: int = 0) -> None`
# 7. Przyjmij górny lewy róg ekranu za punkt początkowy:
#    - idąc w prawo dodajesz `x`
#    - idąc w lewo odejmujesz `x`
#    - idąc w górę odejmujesz `y`
#    - idąc w dół dodajesz `y`
# 8. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code



class Position:
    def __init__(self, x=0, y=0):
        self.point = Point(x, y)

    def set_position(self, x, y):
        self.point.x = x
        self.point.y = y

    def get_position(self):
        return self.point

    def change_position(self, left: int = 0, right: int = 0, up: int = 0, down: int = 0) -> None:
        current = self.get_position()
        new_x = current.x + right - left
        new_y = current.y + down - up
        self.set_position(new_x, new_y)
