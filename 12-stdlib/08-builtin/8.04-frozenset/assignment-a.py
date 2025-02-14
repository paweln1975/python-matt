"""
Name: Sequence Frozenset Create
Difficulty: easy
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

>>> assert result_a is not Ellipsis, \
'Assign result to variable: `result_a`'
>>> assert result_b is not Ellipsis, \
'Assign result to variable: `result_b`'
>>> assert result_c is not Ellipsis, \
'Assign result to variable: `result_c`'
>>> assert result_d is not Ellipsis, \
'Assign result to variable: `result_d`'
>>> assert result_e is not Ellipsis, \
'Assign result to variable: `result_e`'

>>> assert type(result_a) is frozenset, \
'Variable `result_a` has invalid type, should be frozenset'
>>> assert type(result_b) is frozenset, \
'Variable `result_b` has invalid type, should be frozenset'
>>> assert type(result_c) is frozenset, \
'Variable `result_c` has invalid type, should be frozenset'
>>> assert type(result_d) is frozenset, \
'Variable `result_d` has invalid type, should be frozenset'
>>> assert type(result_e) is frozenset, \
'Variable `result_e` has invalid type, should be frozenset'

>>> assert result_a == frozenset({1, 2, 3}), \
'Variable `result_a` has invalid value, should be frozenset({1, 2, 3})'
>>> assert result_b == frozenset({1.1, 2.2, 3.3}), \
'Variable `result_b` has invalid value, should be frozenset({1.1, 2.2, 3.3})'
>>> assert result_c == frozenset({'a', 'b', 'c'}), \
'Variable `result_c` has invalid value, should be frozenset({"a", "b", "c"})'
>>> assert result_d == frozenset({True, False}), \
'Variable `result_d` has invalid value, should be frozenset({True, False})'
>>> assert result_e == frozenset({1, 2.2, True, 'a'}), \
'Variable `result_e` has invalid value, should be frozenset({1, 2.2, True, "a"})'

"""

# %% SetUp

result_a: frozenset[int]
result_b: frozenset[float]
result_c: frozenset[str]
result_d: frozenset[bool]
result_e: frozenset[int|float|bool|str]

# English
# 1. Create frozensets:
#    - `result_a` with elements: 1, 2, 3
#    - `result_b` with elements: 1.1, 2.2, 3.3
#    - `result_c` with elements: 'a', 'b', 'c'
#    - `result_d` with elements: True, False
#    - `result_e` with elements: 1, 2.2, True, 'a'
# 2. Run doctests - all must succeed

# Polish
# 1. Stwórz frozensety:
#    - `result_a` z elementami: 1, 2, 3
#    - `result_b` z elementami: 1.1, 2.2, 3.3
#    - `result_c` z elementami: 'a', 'b', 'c'
#    - `result_d` z elementami: True, False, True
#    - `result_e` z elementami: 1, 2.2, True, 'a'
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result_a = ...
result_b = ...
result_c = ...
result_d = ...
result_e = ...