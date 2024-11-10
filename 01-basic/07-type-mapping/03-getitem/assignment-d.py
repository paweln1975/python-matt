"""
* Assignment: Mapping Dict Switch
* Type: class assignment
* Complexity: medium
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Use `DATA: dict` - with pilot's phonetic alphabet
    2. Ask user to input letter
    3. Define `result: str` with phonetic pronunciation of a letter
    4. If character not existing in alphabet, assign: 'Missing'
    5. Non-functional requirements:
        a. User will always put only one capitalized letter
        b. User will not input any invalid characters or numbers
        c. Do not use `if`, `try`, and `except`
        d. `Mock` will simulate inputting `W` letter by a user
        e. Use `input()` function as normal
    6. Run doctests - all must succeed

Polish:
    1. Użyj `DATA: dict` - alfabet fonetyczny pilotów
    2. Poproś użytkownika o wprowadzenie litery
    3. Zdefiniuj `result: str` z fonetyczną wymową litery
    4. Jeżeli znak nie istnieje w alfabecie, przypisz: 'Missing'
    5. Wymagania niefunkcjonalne:
        a. Użytkownik zawsze wpisze tylko jedną wielką literę lub cyfrę
        b. Nie używaj `if`, `try`, i `except`
        c. `Mock` zasymuluje wpisanie litery `W` przez użytkownika
        d. Skorzytaj z funkcji `input()` tak jak normalnie
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * input(prompt)

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

    >>> pprint(result)
    'Whisky'
"""

# Simulate user input (for test automation)
from unittest.mock import Mock
input = Mock(return_value='W')


DATA = {
    'A': 'Alfa',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliet',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whisky',
    'X': 'X-Ray',
    'Z': 'Zulu',
}

# Ask user to input letter
# type: str
letter = input("Letter: ")

# Define `result: str` with phonetic pronunciation of a letter
# If character not existing in alphabet, assign: 'Missing'
# type: str
result = DATA.get(letter, 'Missing')

