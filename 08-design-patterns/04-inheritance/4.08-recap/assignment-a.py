"""
Name: Inheritance Recap Decomposition
Difficulty: easy
Lines: 30
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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from random import seed; seed(0)
>>> from inspect import isclass

>>> assert isclass(Hero)
>>> assert isclass(HasHealth)
>>> assert isclass(HasPosition)
>>> assert issubclass(Hero, HasHealth)
>>> assert issubclass(Hero, HasPosition)
>>> assert hasattr(HasHealth, 'health')
>>> assert hasattr(HasHealth, 'is_alive')
>>> assert hasattr(HasHealth, 'is_dead')
>>> assert hasattr(HasPosition, 'position_x')
>>> assert hasattr(HasPosition, 'position_y')
>>> assert hasattr(HasPosition, 'position_set')
>>> assert hasattr(HasPosition, 'position_change')
>>> assert hasattr(HasPosition, 'position_get')
>>> assert hasattr(Hero, 'HEALTH_MIN')
>>> assert hasattr(Hero, 'HEALTH_MAX')
>>> assert hasattr(Hero, 'health')
>>> assert hasattr(Hero, 'position_x')
>>> assert hasattr(Hero, 'position_y')
>>> assert hasattr(Hero, 'is_alive')
>>> assert hasattr(Hero, 'is_dead')
>>> assert hasattr(Hero, 'position_set')
>>> assert hasattr(Hero, 'position_change')
>>> assert hasattr(Hero, 'position_get')
>>> watney = Hero()
>>> watney.is_alive()
True
>>> watney.position_set(x=1, y=2)
>>> watney.position_change(left=1, up=2)
>>> watney.position_get()
(0, 0)
>>> watney.position_change(right=1, down=2)
>>> watney.position_get()
(1, 2)

"""

# %% SetUp

from typing import ClassVar
from dataclasses import dataclass
from random import randint

Hero: type
HasHealth: type
HasPosition: type

# English
# 1. Refactor class `Hero` to use multiple inheritance
# 2. Name mixin classes: `HasHealth` and `HasPosition`
# 3. Note, that order of inheritance is important
#    - Try to inherit from `HasPosition`, `HasHealth`
#    - Then `HasHealth`, `HasPosition`
#    - What changed and why?
# 4. Run doctests - all must succeed

# Polish
# 1. Zrefaktoruj klasę `Hero` aby użyć wielodziedziczenia
# 2. Nazwij klasy domieszkowe: `HasHealth` i `HasPosition`
# 3. Zwróć uwagę, że kolejność dziedziczenia ma znaczenie
#    - Spróbuj dziedziczyć po `HasPosition`, `HasHealth`
#    - A później `HasHealth`, `HasPosition`
#    - Co się zmieniło i dlaczego?
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class Hero:
    HEALTH_MIN: ClassVar[int] = 10
    HEALTH_MAX: ClassVar[int] = 20
    health: int = 0
    position_x: int = 0
    position_y: int = 0

    def position_set(self, x: int, y: int) -> None:
        self.position_x = x
        self.position_y = y

    def position_change(self, right=0, left=0, down=0, up=0):
        x = self.position_x + right - left
        y = self.position_y + down - up
        self.position_set(x, y)

    def position_get(self) -> tuple:
        return self.position_x, self.position_y

    def __post_init__(self) -> None:
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)

    def is_alive(self) -> bool:
        return self.health > 0

    def is_dead(self) -> bool:
        return self.health <= 0