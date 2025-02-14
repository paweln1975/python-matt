"""
Name: OOP ObjectRelations Syntax
Difficulty: easy
Lines: 7
Minutes: 5

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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> from inspect import isclass

>>> assert isclass(Point)
>>> assert isclass(Path)
>>> assert hasattr(Point, 'x')
>>> assert hasattr(Point, 'y')

>>> Point()
Point(x=0, y=0)
>>> Point(x=0, y=0)
Point(x=0, y=0)
>>> Point(x=1, y=2)
Point(x=1, y=2)

>>> Path([Point(x=0, y=0),
...       Point(x=0, y=1),
...       Point(x=1, y=0)])
Path(points=[Point(x=0, y=0), Point(x=0, y=1), Point(x=1, y=0)])

"""

# %% SetUp

from dataclasses import dataclass, field

Point: type
Path: type

# English
# 1. Use Dataclass to define class `Point` with attributes:
#    - `x: int` with default value `0`
#    - `y: int` with default value `0`
# 2. Use Dataclass to define class `Path` with attributes:
#    - `points: list[Point]` with default empty list
# 3. Run doctests - all must succeed

# Polish
# 1. Użyj Dataclass do zdefiniowania klasy `Point` z atrybutami:
#    - `x: int` z domyślną wartością `0`
#    - `y: int` z domyślną wartością `0`
# 2. Użyj Dataclass do zdefiniowania klasy `Path` z atrybutami:
#    - `points: list[Point]` z domyślną pustą listą
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
