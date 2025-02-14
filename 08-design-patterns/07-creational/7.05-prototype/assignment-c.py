"""
Name: DesignPatterns Creational PrototypeDragon
Difficulty: easy
Lines: 6
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from pprint import pprint
>>> from random import seed
>>> seed(0)

>>> dragon = Dragon('Wawelski')
>>> result = dragon.clone()

>>> result.name
'Wawelski'

>>> result.health
74

>>> result.gold
98

>>> result.position
(0, 0)

"""

# %% SetUp

from dataclasses import dataclass, field
from random import randint, seed

from typing import Callable
Dragon: type
clone: Callable[[object], object]

seed(0)

# English
# 1. Create class `Dragon`
# 2. Dragon has attributes:
#    - `name: str`
#    - `position: tuple[int,int]` default `(0, 0)`
#    - `health: int` random from 50 to 100
#    - `gold: int` random from 1 to 100
#    - method `.clone()`
# 3. Method `.clone()` returns another `Dragon` with the same values
# 4. Use `random.randint()` to generate pseudorandom numbers
# 5. Run doctests - all must succeed

# Polish
# 1. Stwórz klasę `Dragon`
# 2. Dragon ma atrybuty:
#    - `name: str`
#    - `position: tuple[int,int]` domyślnie `(0, 0)`
#    - `health: int` losowe od 50 do 100
#    - `gold: int` losowe od 1 do 100
#    - metodę `.clone()`
# 3. Metoda `.clone()` zwraca kolejnego `Dragon` z tymi samymi wartościami
# 4. Użyj `random.randint()` do generowania pseudolosowych liczb
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class Dragon:
    ...