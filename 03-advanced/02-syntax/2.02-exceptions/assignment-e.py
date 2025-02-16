"""
Name: Syntax Exception IsDead
Difficulty: easy
Lines: 4
Minutes: 3

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
Terminal: `python -m doctest -v assignment-e.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass

>>> isclass(Hero.IsDead)
True
>>> issubclass(Hero.IsDead, Exception)
True

>>> hero = Hero('Mark Watney')
>>> hero.take_damage(1)

>>> try:
...     hero.take_damage(20)
... except hero.IsDead:
...     True
True

>>> hero = Hero('Mellisa Lewis')

>>> try:
...     hero.take_damage(10)
... except hero.IsDead:
...     True
True

Hints:
`class`
`pass`
`raise`
`if`

"""

# %% SetUp

# English
# 1. Modify `Hero` class
# 2. Add new exception `IsDead` inside `Hero` class
# 3. If `health` is equal or lower than 0, raise `IsDead`
# 4. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `Hero`
# 2. Dodaj nowy wyjątek `IsDead` wewnątrz klasy `Hero`
# 3. Jeżeli `health` jest równy lub mniejszy niż 0, podnieś `IsDead`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 10

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            raise self.IsDead


    class IsDead(Exception):
        pass