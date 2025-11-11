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

>>> main(Platform.Linux)
Linux Textbox username
Linux Textbox password
Linux Button submit

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

# abstract products
class Button(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def render(self):
        pass

class TextBox(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def render(self):
        pass


# concrete products
class LinuxButton(Button):
    def render(self):
        print(f'Linux Button {self.name}')

class LinuxTextBox(TextBox):
    def render(self):
        print(f'Linux Textbox {self.name}')

class AndroidButton(Button):
    def render(self):
        print(f'Android Button {self.name}')

class AndroidTextBox(TextBox):
    def render(self):
        print(f'Android Textbox {self.name}')

# abstract factory
class OSFactory(ABC):

    @abstractmethod
    def create_button(self, name: str) -> Button:
        raise NotImplementedError()

    @abstractmethod
    def create_text_box(self, name: str) -> TextBox:
        raise NotImplementedError()

# concrete factories
class LinuxFactory(OSFactory):
    def create_button(self, name: str) -> Button:
        return LinuxButton(name)

    def create_text_box(self, name: str) -> TextBox:
        return LinuxTextBox(name)

class AndroidFactory(OSFactory):
    def create_button(self, name: str) -> Button:
        return AndroidButton(name)

    def create_text_box(self, name: str) -> TextBox:
        return AndroidTextBox(name)

class Platform(Enum):
    Linux = LinuxFactory()
    Android = AndroidFactory()

def main(platform: Platform):
    factory = platform.value
    factory.create_text_box('username').render()
    factory.create_text_box('password').render()
    factory.create_button('submit').render()
