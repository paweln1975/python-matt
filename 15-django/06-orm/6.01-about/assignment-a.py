"""
Name: Database ORM Import
Difficulty: easy
Lines: 2
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
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

"""

# %% SetUp

import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'

# get the current working directory
current_working_directory = os.getcwd()

# print output to the console
print(current_working_directory)

import django; django.setup()
from demo.models import Role



Role.objects.all().delete()

ROLES = [
    {"name": "Admin", "comment": "Alfa"},
    {"name": "User", "comment": "Bravo"},
    {"name": "Root", "comment": "Charlie"}
]

# English
# 0. Use `myproject.shop`
# 1. Import data from `PRODUCTS`
# 2. Non-functional requirements:
#    - You may use any Python standard library module
#    - You can use Django with migrations
#    - Do not install any additional packages

# Polish
# 0. Użyj `myproject.shop`
# 1. Zaimportuj dane z `PRODUCTS`
# 2. Wymagania niefunkcjonalne:
#    - Możesz użyć dowolnego modułu z biblioteki standardowej
#    - Możesz użyć Django
#    - Nie instaluj ani nie używaj dodatkowych pakietów

# %% Result

for role in ROLES:
    Role.objects.create(**role)