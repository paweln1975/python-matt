"""
* Assignment: DesignPatterns Creational AbstractFactory
* Complexity: easy
* Lines of code: 70 lines
* Time: 21 min

English:
    1. Implement Abstract Factory pattern
    2. Run doctests - all must succeed

Polish:
    1. Zaimplementuj wzorzec Abstract Factory
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
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
from dataclasses import dataclass
from enum import Enum


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


