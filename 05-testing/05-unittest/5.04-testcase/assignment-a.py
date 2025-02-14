"""
Name: DevOps Unittest Rectangle
Difficulty: medium
Lines: 100
Minutes: 21

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

"""

# %% SetUp

from unittest import TestCase

Rectangle: type
RectangleTest: type[TestCase]

class Rectangle:

    def __init__(self, a, b):
        self.side_a = a
        self.side_b = b

        if a <= 0 or b <= 0:
            raise ValueError('Side length must be positive')

    def area(self) -> int:
        return self.side_a * self.side_b

    def circumference(self) -> int:
        return (self.side_a + self.side_b) * 2

    def __str__(self):
        return f'Rectangle({self.side_a}, {self.side_b})'

# English
# 1. Write unittest for `Rectangle`
# 2. Run unittest - all must succeed

# Polish
# 1. Napisz testy jednostkowe dla `Rectangle`
# 2. Uruchom unittest - wszystkie muszą się powieść

# %% Result
