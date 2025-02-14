"""
Name: Loop WhileElse Found
Difficulty: medium
Lines: 5
Minutes: 5

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0

Hints:
`Stop` or `Ctrl+C` kills infinite loop

"""

# %% SetUp

from unittest.mock import MagicMock

HIDDEN = 4
MAX_TRIES = 4

# English
# 1. Modify game code below
# 2. User can try `MAX_TRIES` times, if he/sh does not guess number by then
#    print `Game over, max tries achieved.`
# 3. Don't use `while ... else` syntax
# 4. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj kod gry poniżej
# 2. Użytkownik może próbować `MAX_TRIES` razy, jeżeli w tym czasie nie zgadnie
#    to wypisz `Game over, max tries achieved.`
# 3. Nie używaj składni `while ... else`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
input = MagicMock(side_effect=['0', '9', '1', '8', '2', '7', '3', '6', '4'])

while True:
    guess = input('\nType number: ')

    if int(guess) > HIDDEN:
        print('Above')
    elif int(guess) < HIDDEN:
        print('Below')
    else:
        print('Exactly')
        break