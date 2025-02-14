"""
Name: DesignPatterns Creational AbstractFactory
Difficulty: easy
Lines: 70
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
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from pprint import pprint

>>> main(Platform.iOS)
iOS Textbox username
iOS Textbox password
iOS Button submit

>>> main(Platform.Android)
Android Textbox username
Android Textbox password
Android Button submit

"""

# %% SetUp

from dataclasses import dataclass
from enum import Enum
from abc import ABC, abstractmethod

# English
# 1. Implement Abstract Factory pattern
# 2. Run doctests - all must succeed

# Polish
# 1. Zaimplementuj wzorzec Abstract Factory
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Platform(Enum):
    iOS = 'iOS'
    Android = 'Android'

@dataclass
class Button:
    name: str

    def render(self, platform: Platform):
        if platform is platform.iOS:
            print(f'iOS Button {self.name}')
        elif platform is platform.Android:
            print(f'Android Button {self.name}')

@dataclass
class Textbox:
    name: str

    def render(self, platform: Platform):
        if platform is platform.iOS:
            print(f'iOS Textbox {self.name}')
        elif platform is platform.Android:
            print(f'Android Textbox {self.name}')

def main(platform: Platform):
    Textbox('username').render(platform)
    Textbox('password').render(platform)
    Button('submit').render(platform)