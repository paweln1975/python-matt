"""
* Assignment: Mapping Dict SwitchMissing
* Type: class assignment
* Complexity: medium
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Use `DATA: dict` with Polish diacritic characters
    2. Ask user to input single letter
    3. Convert letter to lowercase
    4. If letter is in `DATA` then use conversion value for the letter
    5. Non-functional requirements:
        a. User will always put only one capitalized letter
        b. User will not input any invalid characters or numbers
        c. Do not use `if`, `try`, and `except`
        d. Use `input()` function as normal
        e. `Mock` will simulate inputting `O` letter by a user
        f. Note that letter `O` is not in `DATA`
    6. Run doctests - all must succeed

Polish:
    1. Użyj `DATA: dict` z polskimi znakami diakrytycznymi
    2. Poproś użytkownika o wprowadzenie pojedynczej litery
    3. Zamień literę na małą
    4. Jeżeli litera jest w `DATA` to użyj wartości konwersji dla litery
    5. Wymagania niefunkcjonalne:
        a. Użytkownik zawsze wpisze tylko jedną wielką literę
        b. Użytkownik nie wpisze żadnych nieprawidłowych znaków lub cyfr
        c. Nie używaj `if`, `try`, i `except`
        d. Skorzytaj z funkcji `input()` tak jak normalnie
        e. `Mock` zasymuluje wpisanie litery `O` przez użytkownika
        f. Zwróć uwagę, że litera `O` nie jest w `DATA`
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * input()
    * str.lower()

Example:
    | Input | Output |
    |-------|--------|
    |   a   |    a   |
    |   A   |    a   |
    |   ą   |    a   |
    |   Ą   |    a   |
    |   b   |    b   |
    |   B   |    B   |
    |   c   |    c   |
    |   C   |    c   |
    |   ć   |    c   |
    |   Ć   |    c   |
    |  ...  |   ...  |

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> import string

    >>> assert letter is not Ellipsis, \
    'Ask user to input letter and assign it to: `letter`'
    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'
    >>> assert result not in DATA.keys(), \
    'Result should not be in DATA dict'
    >>> assert result in string.ascii_letters, \
    'Result should be an ASCII letter'

    >>> pprint(result)
    'o'
"""

# Simulate user input (for test automation)
from unittest.mock import Mock
input = Mock(side_effect=['O'])


DATA = {
    'ą': 'a',
    'ć': 'c',
    'ę': 'e',
    'ł': 'l',
    'ń': 'n',
    'ó': 'o',
    'ś': 's',
    'ż': 'z',
    'ź': 'z',
}

# Ask user to input single letter
# Convert letter to lowercase
# type: str
letter = input("Letter: ")
letter = str(letter).lower()

# If letter is in `DATA` then use conversion value for the letter
# type: str
result = DATA.get(letter, letter)

