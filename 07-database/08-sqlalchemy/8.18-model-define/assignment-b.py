"""
Name: Model Define UserAddress
Difficulty: medium
Lines: 20
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
Terminal: `python -m doctest -v assignment-b.py`

Tests:

"""

# %% SetUp

# English
# 1. Create model `User` with fields:
#    - firstname - first name
#    - lastname - last name
#    - birthdate - date of birth
#    - ssn - PESEL
#    - email - email address
#    - phone - phone number with country code
# 2. Create model `Address` with fields:
#    - type - address type: billing, delivery
#    - street - street, house number, apartment number
#    - postcode - postal code
#    - city - city
#    - region - region or state
#    - country - country
# 3. Functional requirements:
#    - Address may not have street or postal code
# 4. Non-functional requirements:
#    - Use SQLAlchemy ORM to create models
#    - Add `id` fields if needed
#    - You can use any module from standard library
#    - You can use SQLAlchemy and Alembic
#    - Do not install or use additional packages

# Polish
# 1. Stwórz model `User` z polami:
#    - firstname - imię
#    - lastname - nazwisko
#    - birthdate - data urodzenia
#    - ssn - PESEL
#    - email - adres email
#    - phone - telefon z numerem kierunkowym kraju
# 2. Stwórz model `Address` z polami:
#    - type - rodzaj adresu: rozliczeniowy, dostawy
#    - street - ulica, numer domu, numer mieszkania
#    - postcode - kod pocztowy
#    - city - miasto
#    - region - województwo lub stan
#    - country - kraj
# 3. Wymagania funkcjonalne:
#    - Adres może nie mieć ulicy lub kodu pocztowego
# 4. Wymagania niefunkcjonalne:
#    - Użyj SQLAlchemy ORM do stworzenia modeli
#    - Dodaj pola `id` jeżeli są potrzebne
#    - Możesz użyć dowolnego modułu z biblioteki standardowej
#    - Możesz użyć SQLAlchemy i Alembic
#    - Nie instaluj ani nie używaj dodatkowych pakietów

# %% Result
