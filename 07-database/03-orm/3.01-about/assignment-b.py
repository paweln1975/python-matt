"""
Name: OOP ObjectRelations HasPosition
Difficulty: easy
Lines: 18
Minutes: 8

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> from inspect import isclass, ismethod

>>> assert isclass(Point)
>>> assert isclass(HasPosition)
>>> assert hasattr(Point, 'x')
>>> assert hasattr(Point, 'y')
>>> assert hasattr(HasPosition, 'get_position')
>>> assert hasattr(HasPosition, 'set_position')
>>> assert hasattr(HasPosition, 'change_position')
>>> assert ismethod(HasPosition().get_position)
>>> assert ismethod(HasPosition().set_position)
>>> assert ismethod(HasPosition().change_position)

>>> class User(HasPosition):
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

# %% SetUp

from dataclasses import dataclass

Point: type
HasPosition: type

# English
# 1. Define class `Point`
# 2. Class `Point` has attributes `x: int = 0` and `y: int = 0`
# 3. Define class `HasPosition`
# 4. In `HasPosition` define method `get_position(self) -> Point`
# 5. In `HasPosition` define method `set_position(self, x: int, y: int) -> None`
# 6. In `HasPosition` define method `change_position(self, left: int = 0, right: int = 0, up: int = 0, down: int = 0) -> None`
# 7. Assume left-top screen corner as a initial coordinates position:
#    - going right add to `x`
#    - going left subtract from `x`
#    - going up subtract from `y`
#    - going down add to `y`
# 8. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj klasę `Point`
# 2. Klasa `Point` ma atrybuty `x: int = 0` oraz `y: int = 0`
# 3. Zdefiniuj klasę `HasPosition`
# 4. W `HasPosition` zdefiniuj metodę `get_position(self) -> Point`
# 5. W `HasPosition` zdefiniuj metodę `set_position(self, x: int, y: int) -> None`
# 6. W `HasPosition` zdefiniuj metodę `change_position(self, left: int = 0, right: int = 0, up: int = 0, down: int = 0) -> None`
# 7. Przyjmij górny lewy róg ekranu za punkt początkowy:
#    - idąc w prawo dodajesz `x`
#    - idąc w lewo odejmujesz `x`
#    - idąc w górę odejmujesz `y`
#    - idąc w dół dodajesz `y`
# 8. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
