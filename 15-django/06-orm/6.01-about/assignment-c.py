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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 10), \
'Python 3.10+ required'

"""

# %% SetUp

import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
import django; django.setup()
from shop.models import Customer, Address

Address.objects.all().delete()

ADDRESSES = [
  {
    "customer": "mwatney@nasa.gov",
    "type": "billing",
    "street": "2101 E NASA Pkwy",
    "city": "Houston",
    "postcode": "77058",
    "region": "Texas",
    "country": "USA"
  },
  {
    "customer": "mwatney@nasa.gov",
    "type": "shipping",
    "street": "",
    "city": "Kennedy Space Center",
    "postcode": "32899",
    "region": "Florida",
    "country": "USA"
  },
  {
    "customer": "mlewis@nasa.gov",
    "type": "shipping",
    "street": "Kamienica Pod św. Janem Kapistranem",
    "city": "Kraków",
    "postcode": "31008",
    "region": "Małopolskie",
    "country": "Poland"
  },
  {
    "customer": "rmartinez@nasa.gov",
    "type": "billing",
    "street": "",
    "city": "Звёздный городо́к",
    "postcode": "141160",
    "region": "Московская область",
    "country": "Россия"
  },
  {
    "customer": "rmartinez@nasa.gov",
    "type": "shipping",
    "street": "",
    "city": "Космодро́м Байкону́р",
    "postcode": "",
    "region": "Кызылординская область",
    "country": "Қазақстан"
  },
  {
    "customer": "avogel@esa.int",
    "type": "shipping",
    "street": "Linder Hoehe",
    "city": "Cologne",
    "postcode": "51147",
    "region": "North Rhine-Westphalia",
    "country": "Germany"
  },
  {
    "customer": "bjohanssen@nasa.gov",
    "type": "shipping",
    "street": "2825 E Ave P",
    "city": "Palmdale",
    "postcode": "93550",
    "region": "California",
    "country": "USA"
  },
  {
    "customer": "cbeck@nasa.gov",
    "type": "shipping",
    "street": "4800 Oak Grove Dr",
    "city": "Pasadena",
    "postcode": "91109",
    "region": "California",
    "country": "USA"
  }
]

# English
# 0. Use `myproject.shop`
# 1. Import data from `ADDRESSES`
# 2. Non-functional requirements:
#    - You may use any Python standard library module
#    - You can use Django with migrations
#    - Do not install any additional packages

# Polish
# 0. Użyj `myproject.shop`
# 1. Zaimportuj dane z `ADDRESSES`
# 2. Wymagania niefunkcjonalne:
#    - Możesz użyć dowolnego modułu z biblioteki standardowej
#    - Możesz użyć Django
#    - Nie instaluj ani nie używaj dodatkowych pakietów

# %% Result
