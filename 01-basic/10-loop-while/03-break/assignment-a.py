
"""
* Assignment: Loop While GuessGame1
* Type: homework
* Complexity: medium
* Lines of code: 9 lines
* Time: 5 min

English:
    1. Use `input` in `while True` loop to ask user about number
    2. Compare user's number with `HIDDEN`:
       a. If number is equal, print `Exactly` and break game
       b. If number is greater, print `Above`
       c. If number is lower, print `Below`
    3. Non-functional requirements:
        a. User will always input only one digit
        b. User will not input any invalid characters or longer numbers
        c. `Mock` will simulate inputting numbers by a user
        d. Use `input()` function as normal
    4. Run doctests - all must succeed

Polish:
    1. Użyj `input` w pętli `while True` do pytania użytkownika o liczbę
    2. Porównaj liczbę wprowadzoną przez użytkownika z `HIDDEN`:
       a. Jeżeli jest taka sama, to wypisz `Exactly` i zakończ grę
       b. Jeżeli jest większa, to wypisz `Above`
       c. Jeżeli jest mniejsza, to wypisz `Below`
    3. Wymagania niefunkcjonalne:
        a. Użytkownik zawsze wpisze tylko jedną cyfrę
        b. Użytkownik nie wpisze żadnych nieprawidłowych znaków lub dłuższych liczb
        c. `Mock` zasymuluje wpisanie liczb przez użytkownika
        d. Skorzytaj z funkcji `input()` tak jak normalnie
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `Stop` or `Ctrl+C` kills infinite loop

Tests:
    >>> import sys; sys.tracebacklimit = 0
"""

# Following two lines is needed for test automation
# In your code use `input()` function as normal
# `Mock` will simulate inputting numbers by a user
# So that, first number is `0`, second is `9`, and so on
from unittest.mock import Mock
input = Mock(side_effect=['0', '9', '1', '8', '2', '7', '3', '6', '4'])


HIDDEN = 4

while True:
    digit = int(input('Enter digit:'))
    if digit == HIDDEN:
        break
    elif digit < HIDDEN:
        print('Below')
    elif digit > HIDDEN:
        print('Above')

