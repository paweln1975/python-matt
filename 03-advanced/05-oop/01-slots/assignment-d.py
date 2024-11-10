"""
* Assignment: OOP AttributeSlots Init
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define function `dump(obj) -> dict` accepting instance with slots
    2. Function should return similar output to `vars()`, i.e.:
       {'firstname':'mwatney', 'lastname':'Ares3'}
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `dump(obj) -> dict` przyjmującą instancję ze slotami
    2. Funkcja powinna zwracać podobny wynik do `vars()`, np:
       {'firstname':'mwatney', 'lastname':'Ares3'}
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from dataclasses import is_dataclass

    >>> class User:
    ...     __slots__ = ('firstname', 'lastname')
    ...
    ...     def __init__(self, firstname, lastname):
    ...         self.firstname = firstname
    ...         self.lastname = lastname
    >>>
    >>>
    >>> mark = User(firstname='Mark', lastname='Watney')
    >>> result = dump(mark)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is dict, \
    'Result must be a type'
    >>> assert len(result) == 2, \
    'Result length must be 2'
    >>> assert all(type(x) is str for x in result.keys()), \
    'All keys in result must be a str'
    >>> assert all(type(x) is str for x in result.values()), \
    'All values in result must be a str'

    >>> result
    {'firstname': 'Mark', 'lastname': 'Watney'}
"""

# Define function `dump(obj) -> dict` accepting instance with slots
# Function should return similar output to `vars()`
# type: Callable[[object], dict]
def dump(obj) -> dict:
    ...


