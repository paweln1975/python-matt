"""
* Assignment: Exception New IsDead
* Type: homework
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Modify `Hero` class
    2. Add new exception `IsDead` inside `Hero` class
    3. If `health` is equal or lower than 0, raise `IsDead`
    4. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `Hero`
    2. Dodaj nowy wyjątek `IsDead` wewnątrz klasy `Hero`
    3. Jeżeli `health` jest równy lub mniejszy niż 0, podnieś `IsDead`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `class`
    * `pass`
    * `raise`
    * `if`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> isclass(Hero.IsDead)
    True
    >>> issubclass(Hero.IsDead, Exception)
    True

    >>> hero = Hero('Mark Watney')
    >>> hero.take_damage(1)

    >>> try:
    ...     hero.take_damage(20)
    ... except hero.IsDead:
    ...     True
    True
"""

# Modify `Hero` class
# Add custom exception `IsDead` inside `Hero` class
# If `health` is equal or lower than 0, raise `IsDead`
# type: type[Hero]
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 10

    def take_damage(self, damage):
        self.health -= damage


