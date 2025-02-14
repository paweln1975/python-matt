"""
Name: Syntax AssignmentExpression Users
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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert result is not Ellipsis, \
'Assign result to variable: `result`'
>>> assert len(result) > 0, \
'Variable `result` cannot be empty'
>>> assert type(result) is list, \
'Variable `result` has invalid type, should be list'
>>> assert all(type(x) is tuple for x in result), \
'All rows in `result` should be tuple'

>>> from pprint import pprint
>>> pprint(result)
[('Mark', 'Watney'),
 ('Melissa', 'Lewis'),
 ('Rick', 'Martinez'),
 ('Alex', 'Vogel'),
 ('Chris', 'Beck'),
 ('Beth', 'Johanssen')]

Hints:
`str.splitlines()`
`str.split()`

"""

# %% SetUp

result: list[tuple[str,str]]

DATA = """firstname,lastname,age
Mark,Watney,41
Melissa,Lewis,40
Rick,Martinez,39
Alex,Vogel,40
Chris,Beck,36
Beth,Johanssen,29
"""

header, *lines = DATA.splitlines()

# English
# 1. Define `result: list[tuple]` with user's firstname and lastname,
#    example: [('Mark', 'Watney'), ('Melissa', 'Lewis'), ...]
# 2. Skip the header: ('firstname', 'lastname')
# 3. Use assignment expression in a list comprehension
# 4. Run doctests - all must succeed

# Polish
# 1. Zdefiniuj `result: list[tuple]` z imionami i nazwiskami użytkowników
#    przykład: [('Mark', 'Watney'), ('Melissa', 'Lewis'), ...]
# 2. Pomiń nagłówek: ('firstname', 'lastname')
# 3. Użyj assignment expression w list comprehension
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...