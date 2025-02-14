"""
Name: DataFrame Create
Difficulty: easy
Lines: 8
Minutes: 3

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
Terminal: `python -m doctest -v assignment-e.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> pd.set_option('display.width', 500)
>>> pd.set_option('display.max_columns', 10)
>>> pd.set_option('display.max_rows', 10)

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert type(result) is pd.DataFrame, \
'Variable `result` must be a `pd.DataFrame` type'

>>> result  # doctest: +NORMALIZE_WHITESPACE
  firstname   lastname       role
0      Mark     Watney   botanist
1   Melissa      Lewis  commander
2      Rick   Martinez      pilot
3      Alex      Vogel    chemist
4      Beth  Johanssen   engineer
5     Chris       Back      medic

Hints:
`pd.DataFrame()`

"""

# %% SetUp

import pandas as pd

result: pd.DataFrame

# | firstname | lastname  | role      |
# |-----------|-----------|-----------|
# | Mark      | Watney    | botanist  |
# | Melissa   | Lewis     | commander |
# | Rick      | Martinez  | pilot     |
# | Alex      | Vogel     | chemist   |
# | Beth      | Johanssen | engineer  |
# | Chris     | Back      | medic     |

# English
# 1. Define variabl `result: with
#    dataframe with columns named `firstname`, `lastname`, `role`
# 2. Use selection with `alt` key in your IDE
#    to convert data to `list[tuple]` format
# 3. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj variabl `result` with
#    dataframe z kolumnami nazwanymi `firstname`, `lastname`, `role`
# 2. Użyj zaznaczania z klawiszem `alt` w Twoim IDE
#    aby przekonwertować dane do formatu `list[tuple]`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...