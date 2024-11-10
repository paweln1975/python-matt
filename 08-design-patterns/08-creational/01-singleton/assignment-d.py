"""
* Assignment: DesignPatterns Creational SingletonLogger
* Complexity: medium
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Create singleton class `Singleton`
    2. Use `Metaclass`
    3. Run doctests - all must succeed

Polish:
    1. Stwórz klasę singleton `Singleton`
    2. Użyj `Metaclass`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> class Logger(metaclass=Singleton):
    ...     pass

    >>> result_a = Logger()
    >>> result_b = Logger()

    >>> result_a is result_b
    True
"""
from typing import Self


class Singleton(type):
    pass


