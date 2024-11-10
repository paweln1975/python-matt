"""
* Assignment: Type Str Input
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Ask user to input his/her name
    2. Define `result: str` with text from user
    3. `Mock` will simulate inputting of name `Mark` by user
    4. Use `input()` function as normal
    5. Run doctests - all must succeed

Polish:
    1. Poproś użytkownika o wprowadzenie imienia
    2. Zdefiniuj `result: str` z tekstem wprowadzonym od użytkownika
    3. `Mock` zasymuluje wpisanie `Mark` przez użytkownika
    4. Skorzytaj z funkcji `input()` tak jak normalnie
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'
    >>> assert input.call_count == 1, \
    'Call `input()` function'
    >>> assert input.call_args, \
    'Ask user the question'

    >>> result
    'Mark'
"""

# Mock will simulate inputting of name `Mark` by user
from unittest.mock import Mock
input = Mock(return_value='Mark')


# Ask user to type NASA
# type: str
result = input('Podaj imię: ')

