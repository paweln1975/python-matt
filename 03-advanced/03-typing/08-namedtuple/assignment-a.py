"""
* Assignment: Typing Annotations NamedTuple
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define `User: NamedTuple` with:
        a. `firstname: str`
        b. `lastname: str`
        c. `age: int`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `User: NamedTuple` z:
        a. `firstname: str`
        b. `lastname: str`
        c. `age: int`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert sys.version_info >= (3, 5), \
    'Python 3.5+ required'

    >>> from typing import get_type_hints
    >>> get_type_hints(User)
    {'firstname': <class 'str'>, 'lastname': <class 'str'>, 'age': <class 'int'>}

    >>> data: User = User(firstname='Mark', lastname='Watney', age=42)
    >>> data
    User(firstname='Mark', lastname='Watney', age=42)

    >>> data: User = User('Mark', 'Watney', 42)
    >>> data
    User(firstname='Mark', lastname='Watney', age=42)

    >>> data: User = ('Mark', 'Watney', 42)
    >>> data
    ('Mark', 'Watney', 42)
"""
from typing import NamedTuple


# Define `User: NamedTuple` with:
# - `firstname: str`
# - `lastname: str`
# - `age: int`
class User:
    ...


