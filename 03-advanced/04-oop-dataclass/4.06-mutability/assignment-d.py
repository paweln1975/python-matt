"""
Name: Dataclass Mutability Randint
Difficulty: easy
Lines: 3
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
Terminal: `python -m doctest -v assignment-d.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass
>>> from random import seed; seed(0)

>>> assert isclass(Hero)
>>> assert hasattr(Hero, '__annotations__')

>>> assert 'name' in Hero.__dataclass_fields__
>>> assert 'health' in Hero.__dataclass_fields__

>>> warrior = Hero('Warrior')
>>> assert warrior.name == 'Warrior'
>>> assert warrior.health == 74

>>> mage = Hero('Mage')
>>> assert mage.name == 'Mage'
>>> assert mage.health == 98

>>> rouge = Hero('Rouge')
>>> assert rouge.name == 'Rouge'
>>> assert rouge.health == 76

>>> cleric = Hero('Cleric')
>>> assert cleric.name == 'Cleric'
>>> assert cleric.health == 52

Hints:
`field(default_factory=lambda:...)`

"""

# %% SetUp

from dataclasses import dataclass, field
from random import randint

Hero: type

# English
# 1. Create class `Hero`, with attributes:
#    - `name: str` (required)
#    - `health: int` (optional), default: randint(50, 100)
# 2. Attributes must be set at the initialization from constructor arguments
# 3. Avoid mutable parameter problem
# 4. Użyj funkcji `randint()` z biblioteki `random`
# 5. Use `dataclass`
# 6. Run doctests - all must succeed

# Polish
# 1. Stwórz klasę `Hero`, z atrybutami:
#    - `name: str` (wymagane)
#    - `health: int` (opcjonalne), domyślnie: randint(50, 100)
# 2. Atrybuty mają być ustawiane przy inicjalizacji z parametrów konstruktora
# 3. Uniknij problemu mutowalnych parametrów
# 4. Użyj funkcji `randint()` z biblioteki `random`
# 5. Użyj `dataclass`
# 6. Uruchom doctesty - wszystkie muszą się powieść

def default_health():
    return randint(50, 100)


# %% Result
@dataclass
class Hero:
    name: str
    health: int = field(default_factory=default_health)