"""
* Assignment: DesignPatterns Creational SingletonSettings
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Create singleton class `Settings`
    2. Use `get_instance()` classmethod
    3. Run doctests - all must succeed

Polish:
    1. Stwórz klasę singleton `Settings`
    2. Użyj metody klasy `get_instance()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> result_a = Settings.get_instance()
    >>> result_b = Settings.get_instance()

    >>> result_a is result_b
    True
"""
from typing import Self


class Settings:
    pass


