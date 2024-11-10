"""
* Assignment: Typing Annotations Mapping
* Complexity: easy
* Lines of code: 4 lines
* Time: 2 min

English:
    1. Define `User: TypedDict` with:
        a. `firstname: str`
        b. `lastname: str`
        c. `age: int`
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `User: TypedDict` z:
        a. `firstname: str`
        b. `lastname: str`
        c. `age: int`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> assert sys.version_info >= (3, 5), \
    'Python 3.5+ required'

    >>> from typing import get_type_hints, is_typeddict
    >>> assert is_typeddict(User), \
    'Class `User` must be a `TypedDict`'

    >>> get_type_hints(User)
    {'firstname': <class 'str'>, 'lastname': <class 'str'>, 'age': <class 'int'>}

    >>> data: User = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
    >>> data
    {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}

    >>> data: User = User(**{'firstname': 'Mark', 'lastname': 'Watney', 'age': 40})
    >>> data
    {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}

    >>> data: User = User(firstname='Mark', lastname='Watney', age=40)
    >>> data
    {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
"""

from typing import TypedDict

# Define `User: TypedDict` with:
# - `firstname: str`
# - `lastname: str`
# - `age: int`
class User:
    ...


