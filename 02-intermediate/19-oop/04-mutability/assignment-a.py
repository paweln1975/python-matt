"""
* Assignment: OOP Mutability list
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Create class `User`, with attributes:
        a. `firstname: str` (required)
        b. `lastname: str` (required)
        c. `groups: list[str]` (optional)
    2. Attributes must be set at the initialization from constructor arguments
    3. Avoid mutable parameter problem
    4. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `User`, z atrybutami:
        a. `firstname: str` (wymagane)
        b. `lastname: str` (wymagane)
        c. `groups: list[str]` (opcjonalne)
    2. Atrybuty mają być ustawiane przy inicjalizacji z parametrów konstruktora
    3. Uniknij problemu mutowalnych parametrów
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert hasattr(User, '__annotations__')

    >>> mark = User('mwatney', 'Ares3')
    >>> melissa = User('mlewis', 'Nasa1')
    >>> assert 'firstname' in vars(mark)
    >>> assert 'lastname' in vars(mark)
    >>> assert 'groups' in vars(mark)
    >>> assert 'firstname' in vars(melissa)
    >>> assert 'lastname' in vars(melissa)
    >>> assert 'groups' in vars(melissa)
    >>> assert mark.groups is not melissa.groups
"""

# Create class `User`, with attributes:
# - `firstname: str` (required)
# - `lastname: str` (required)
# - `groups: list[str]` (optional)
# type: type[User]
class User:
    ...


