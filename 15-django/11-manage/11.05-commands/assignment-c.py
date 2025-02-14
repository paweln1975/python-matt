"""
Name: Django Utils ManagementCommand
Difficulty: medium
Lines: 15
Minutes: 13

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
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

Hints:
`QuerySet.all()`
`django.core.serializers.serialize`
`serialize('json', data, fields=..., indent=2)`

"""

# %% SetUp

# English
# 0. Use `myproject.shop`
# 1. Create management command `shop/management/commands/export_json.py`
# 2. Program exports all `shop.Product` data to JSON format (use stdout)
# 3. For other communication use (stderr)

# Polish
# 0. Użyj `myproject.shop`
# 1. Stwórz komendę zarządzania `shop/management/commands/export_json.py`
# 2. Program eksportuje wszystkie dane `shop.Product` do formatu JSON (użyj stdout)
# 3. Do pozostałej komunikacji użyj (stderr)

# %% Result
