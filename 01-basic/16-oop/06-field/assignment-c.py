"""
* Assignment: OOP Field Vars
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Use instance `mark`
    2. Define `result: dict` with current state of `mark` object
       (all attributes and values in dict format)
    3. Run doctests - all must succeed

Polish:
    1. Użyj instancji `mark`
    2. Zdefiniuj `result: dict` z aktualnym stanem obiektu `mark`
       (wszystkie atrybuty i wartości w formacie dict)
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from inspect import isclass

    >>> assert isclass(User)
    >>> assert isinstance(mark, User)
    >>> assert hasattr(mark, 'firstname')
    >>> assert hasattr(mark, 'lastname')
    >>> assert hasattr(mark, 'is_authenticated')
    >>> assert getattr(mark, 'firstname') == 'Mark'
    >>> assert getattr(mark, 'lastname') == 'Watney'
    >>> assert getattr(mark, 'is_authenticated') is False
"""

class User:
    pass

mark = User()
mark.firstname = 'Mark'
mark.lastname = 'Watney'
mark.is_authenticated = False


# Define `result: dict` with current state of `mark` object
# (all attributes and values in dict format)
# type: dict[str, str|bool]
result = vars(mark)
