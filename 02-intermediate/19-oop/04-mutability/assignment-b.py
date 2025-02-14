
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from random import seed
>>> seed(0)

>>> from inspect import isclass
>>> assert isclass(Hero)
>>> assert hasattr(Hero, '__annotations__')

>>> warrior = Hero('Warrior')
>>> assert warrior.name == 'Warrior'
>>> assert warrior.health == 74

>>> mage = Hero('Mage')
>>> assert mage.name == 'Mage'
>>> assert mage.health == 98

>>> rouge = Hero('Rouge', health=76)
>>> assert rouge.name == 'Rouge'
>>> assert rouge.health == 76

>>> cleric = Hero('Cleric', health=52)
>>> assert cleric.name == 'Cleric'
>>> assert cleric.health == 52
"""
# endregion

# region Show Imports
from random import randint
# endregion

# region Show Types
from typing import Callable
Hero: type
__init__: Callable[[str, int], None]
# endregion

# English
# 1. Create class `Hero`, with attributes:
#    - `name: str` (required)
#    - `health: int` (optional), default: randint(50, 100)
# 2. Attributes must be set at the initialization from constructor arguments
# 3. Avoid mutable parameter problem
# 4. Użyj funkcji `randint()` z biblioteki `random`
# 5. Do not use `dataclass`
# 6. Run doctests - all must succeed

# Polish
# 1. Stwórz klasę `Hero`, z atrybutami:
#    - `name: str` (wymagane)
#    - `health: int` (opcjonalne), domyślnie: randint(50, 100)
# 2. Atrybuty mają być ustawiane przy inicjalizacji z parametrów konstruktora
# 3. Uniknij problemu mutowalnych parametrów
# 4. Użyj funkcji `randint()` z biblioteki `random`
# 5. Nie używaj `dataclass`
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Your code

class Hero:
    def __init__(self, name: str, health: int = None) -> None:
        self.name = name
        self.health = health if health is not None else randint(50, 100)
