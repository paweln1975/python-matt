"""
* Assignment: DesignPatterns Creational SingletonDatabaseConnection
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Create singleton class `Database`
    2. Use `connect()` classmethod
    3. Run doctests - all must succeed

Polish:
    1. Stwórz klasę singleton `Database`
    2. Użyj metody klasy `connect()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> result_a = Database.connect()
    >>> result_b = Database.connect()

    >>> result_a is result_b
    True
"""
from typing import Self


class Database:
    pass


