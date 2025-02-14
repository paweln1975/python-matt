"""
Name: Database ORM Import
Difficulty: easy
Lines: 3
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

"""

# %% SetUp

import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
import django; django.setup()
from shop.models import Customer

Customer.objects.all().delete()

CUSTOMERS = [
  {
    "firstname": "Mark",
    "lastname": "Watney",
    "birthdate": "1994-10-12",
    "gender": "male",
    "tax_number": "94101212345",
    "email": "mwatney@nasa.gov",
    "phone": "+1 (234) 555-0000"
  },
  {
    "firstname": "Melissa",
    "lastname": "Lewis",
    "birthdate": "1995-07-15",
    "gender": "female",
    "tax_number": "95071512345",
    "email": "mlewis@nasa.gov",
    "phone": "+1 (234) 555-0001"
  },
  {
    "firstname": "Rick",
    "lastname": "Martinez",
    "birthdate": "1996-01-21",
    "gender": "male",
    "tax_number": "96012112345",
    "email": "rmartinez@nasa.gov",
    "phone": "+1 (234) 555-0010"
  },
  {
    "firstname": "Alex",
    "lastname": "Vogel",
    "birthdate": "1994-11-15",
    "gender": "male",
    "tax_number": "94111512345",
    "email": "avogel@esa.int",
    "phone": "+49 (234) 555-0011"
  },
  {
    "firstname": "Beth",
    "lastname": "Johanssen",
    "birthdate": "2006-05-09",
    "gender": "female",
    "tax_number": "06250912345",
    "email": "bjohanssen@nasa.gov",
    "phone": "+1 (234) 555-0100"
  },
  {
    "firstname": "Chris",
    "lastname": "Beck",
    "birthdate": "1999-08-02",
    "gender": "male",
    "tax_number": "99080212345",
    "email": "cbeck@nasa.gov",
    "phone": "+1 (234) 555-0101"
  }
]

# English
# 0. Use `myproject.shop`
# 1. Import data from `CUSTOMERS`
# 2. Non-functional requirements:
#    - You may use any Python standard library module
#    - You can use Django with migrations
#    - Do not install any additional packages

# Polish
# 0. Użyj `myproject.shop`
# 1. Zaimportuj dane z `CUSTOMERS`
# 2. Wymagania niefunkcjonalne:
#    - Możesz użyć dowolnego modułu z biblioteki standardowej
#    - Możesz użyć Django
#    - Nie instaluj ani nie używaj dodatkowych pakietów

# %% Result
