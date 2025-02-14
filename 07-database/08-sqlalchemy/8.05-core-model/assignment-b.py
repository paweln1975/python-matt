"""
Name: Model Data AstronautAgency
Difficulty: easy
Lines: 11
Minutes: 8

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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert 'Watney' in vars(watney).values()
>>> assert 'USA' in vars(watney).values()
>>> assert '1969-07-21' in vars(watney).values()
>>> assert 'NASA' in vars(nasa).values()
>>> assert 'USA' in vars(nasa).values()
>>> assert '1958-07-29' in vars(nasa).values()

"""

# %% SetUp

from dataclasses import dataclass

watney: object
nasa: object

# English
# 1. Create propper classes to model the data:
#    - Watney, USA, 1969-07-21
#    - NASA, USA, 1958-07-29
# 2. Create instances (watney, nasa) filling it with data
# 3. Non-functional requirements:
#    - Use SQLAlchemy ORM to create models
#    - Do not convert data, just model it
#    - You can use any Python standard library module
#    - You can use SQLAlchemy and Alembic
#    - Do not install or use 3rd party modules
# 4. Run doctests - all must succeed

# Polish
# 1. Stwórz odpowiednie klasy aby zamodelować dane:
#    - Watney, USA, 1969-07-21
#    - NASA, USA, 1958-07-29
# 2. Stwórz instancje (watney, nasa) wypełniając je danymi
# 3. Wymagania niefunkcjonalne:
#    - Użyj SQLAlchemy ORM do stworzenia modeli
#    - Nie konwertuj danych, tylko je zamodeluj
#    - Możesz użyć dowolnego modułu z biblioteki standardowej
#    - Możesz użyć SQLAlchemy i Alembic
#    - Nie instaluj ani nie używaj dodatkowych pakietów
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
watney = ...
nasa = ...