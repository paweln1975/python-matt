"""
* Assignment: OOP Recap Instance
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Create instance `mark` of a class `Astronaut`
    2. Create instance `nasa` of a class `SpaceAgency`
    3. Run doctests - all must succeed

Polish:
    1. Stwórz instancję `mark` klasy `Astronaut`
    2. Stwórz instancję `nasa` klasy `SpaceAgency`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Astronaut)
    >>> assert isclass(SpaceAgency)
    >>> assert isinstance(mark, Astronaut)
    >>> assert isinstance(nasa, SpaceAgency)
"""

class Astronaut:
    pass


class SpaceAgency:
    pass


# Create instance `mark` of a class `Astronaut`
# type: Astronaut
mark = Astronaut()

# Create instance `nasa` of a class `SpaceAgency`
# type: SpaceAgency
nasa = SpaceAgency()

