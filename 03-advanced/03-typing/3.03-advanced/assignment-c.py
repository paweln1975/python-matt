"""
Name: Typing Annotations Any
Difficulty: easy
Lines: 1
Minutes: 2

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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 5), \
'Python 3.5+ required'

>>> import importlib
>>> from typing import get_type_hints
>>> module = importlib.import_module(__name__)
>>> annotations = get_type_hints(module)

>>> assert annotations['data'] == Any

"""

# %% SetUp

from typing import Any

# English
# 1. Declare type for `data` variable
# 2. Type must match values defined below
# 3. Use `Any` type
# 4. Run doctests - all must succeed

# Polish
# 1. Zadeklaruj typ dla zmiennej `data`
# 2. Typ musi pasować do wartości zdefiniowanych poniżej
# 3. Użyj typu `Any`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
data: Any

# Do not modify lines below
data = 1
data = 1.0
data = 'one'