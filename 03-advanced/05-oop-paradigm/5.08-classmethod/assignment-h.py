"""
Name: OOP MethodClassmethod FromToml
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
Terminal: `python -m doctest -v assignment-h.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from os import remove
>>> from inspect import isclass

>>> assert isclass(Character)
>>> assert isclass(Fighter)
>>> assert isclass(WildMage)
>>> assert isclass(Ranger)
>>> assert isclass(Thief)

>>> DATA = b'''
... [Imoen]
... character_class = 'Thief'
... race = 'Human'
... alignment = 'Neutral Good'
... strength = 9
... dexterity = 18
... constitution = 16
... intelligence = 17
... wisdom = 11
... charisma = 16
...
... [Minsc]
... character_class = 'Ranger'
... race = 'Human'
... alignment = 'Neutral Good'
... strength = 18
... dexterity = 15
... constitution = 15
... intelligence = 8
... wisdom = 6
... charisma = 9
...
... [Neera]
... character_class = 'Wild Mage'
... race = 'Half-elf'
... alignment = 'Chaotic Neutral'
... strength = 11
... dexterity = 17
... constitution = 14
... intelligence = 17
... wisdom = 10
... charisma = 11
...
... [Sarevok]
... character_class = 'Fighter'
... race = 'Human'
... alignment = 'Chaotic Evil'
... strength = 18
... dexterity = 17
... constitution = 18
... intelligence = 17
... wisdom = 10
... charisma = 15
... '''
>>>
>>> with open(FILE, mode='wb') as file:
...     file.write(DATA)
683

>>> imoen = Thief.from_toml(FILE, 'Imoen')
>>> assert type(imoen.character_class) is str
>>> assert type(imoen.race) is str
>>> assert type(imoen.alignment) is str
>>> assert type(imoen.stats) is Stats
>>> assert imoen.character_class == 'Thief'
>>> assert imoen.race == 'Human'
>>> assert imoen.alignment == 'Neutral Good'
>>> assert imoen.stats == Stats(strength=9, dexterity=18,
...                             constitution=16, intelligence=17,
...                             wisdom=11, charisma=16)

>>> minsc = Ranger.from_toml(FILE, 'Minsc')
>>> assert type(minsc.character_class) is str
>>> assert type(minsc.race) is str
>>> assert type(minsc.alignment) is str
>>> assert type(minsc.stats) is Stats
>>> assert minsc.character_class == 'Ranger'
>>> assert minsc.race == 'Human'
>>> assert minsc.alignment == 'Neutral Good'
>>> assert minsc.stats == Stats(strength=18, dexterity=15,
...                             constitution=15, intelligence=8,
...                             wisdom=6, charisma=9)

>>> neera = WildMage.from_toml(FILE, 'Neera')
>>> assert type(neera.character_class) is str
>>> assert type(neera.race) is str
>>> assert type(neera.alignment) is str
>>> assert type(neera.stats) is Stats
>>> assert neera.character_class == 'Wild Mage'
>>> assert neera.race == 'Half-elf'
>>> assert neera.alignment == 'Chaotic Neutral'
>>> assert neera.stats == Stats(strength=11, dexterity=17,
...                             constitution=14, intelligence=17,
...                             wisdom=10, charisma=11)

>>> sarevok = Fighter.from_toml(FILE, 'Sarevok')
>>> assert type(sarevok.character_class) is str
>>> assert type(sarevok.race) is str
>>> assert type(sarevok.alignment) is str
>>> assert type(sarevok.stats) is Stats
>>> assert sarevok.character_class == 'Fighter'
>>> assert sarevok.race == 'Human'
>>> assert sarevok.alignment == 'Chaotic Evil'
>>> assert sarevok.stats == Stats(strength=18, dexterity=17,
...                               constitution=18, intelligence=17,
...                               wisdom=10, charisma=15)

>>> remove(FILE)

Hints:
`open(filename, mode='rb')`
`import tomllib`
`tomllib.load()`

"""

# %% SetUp

import tomllib
from dataclasses import dataclass

from typing import Callable, NamedTuple
Character: type
from_toml: Callable[[type, str, str], object]

FILE = '_temporary.toml'

class Stats(NamedTuple):
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

# English
# 1. Modify class `Character`
# 2. Define classmethod `from_toml()`:
#    - parameter `filename: str`, example: 'myfile.toml'
#    - parameter `name: str`, example: 'Sarevok'
#    - returns instance of a class on which was called
# 3. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `Character`
# 2. Zdefiniuj classmethod `from_toml()`:
#    - parametr `filename: str`, przykład: 'myfile.toml'
#    - parametr `name: str`, przykład: 'Sarevok'
#    - zwraca instancję klasy na której została wykonana
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class Character:
    character_class: str
    race: str
    alignment: str
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    @property
    def stats(self) -> Stats:
        return Stats(
            strength=self.strength,
            dexterity=self.dexterity,
            constitution=self.constitution,
            intelligence=self.intelligence,
            wisdom=self.wisdom,
            charisma=self.charisma)

    @classmethod
    def from_toml(cls, filename: str, name: str):
        with open(filename, 'rb') as f:
            d = tomllib.load(f)

        return cls(**d.get(name))

class Fighter(Character):
    pass

class WildMage(Character):
    pass

class Ranger(Character):
    pass

class Thief(Character):
    pass