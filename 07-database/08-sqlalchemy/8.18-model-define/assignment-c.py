"""
Name: Model Define ProductOrders
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
Terminal: `python -m doctest -v assignment-c.py`

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
#    - phone - phone with country code
# 2. Create model `Address` with fields:
#    - type - type of address: billing, delivery
#    - street - street, house number, apartment number
#    - postcode - postal code
#    - city - city
#    - region - region or state
#    - country - country
# 3. Create model `Product`:
#    - ean13 - EAN-13 barcode
#    - name - Product name
#    - price - Net price
# 4. Create model `Orders`:
#    - user - User
#    - product - Product
# 5. Functional requirements:
#    - User has only one email and one phone
#    - User can have one billing address and one delivery address
#    - Address may not have a street or postal code
#    - User can buy many products
#    - Product could not be purchased
# 6. Non-functional requirements:
#    - Use SQLAlchemy ORM to create models
#    - Add `id` fields if needed
#    - You can use any module from the standard library
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
# 3. Stwórz model `Product`:
#    - ean13 - Kod kreskowy EAN-13
#    - name - Nazwa produktu
#    - price - Cena netto
# 4. Stwórz model `Orders`:
#    - user - Użytkownik
#    - product - Produkt
# 5. Wymagania funkcjonalne:
#    - Użytkownik ma tylko jeden email i jeden telefon
#    - Użytkownik może mieć jeden adres rozliczeniowy i jeden do wysyłki
#    - Adres może nie mieć ulicy lub kodu pocztowego
#    - Użytkownik może zakupić wiele produktów
#    - Produkt mógł nie zostać kupiony
# 6. Wymagania niefunkcjonalne:
#    - Użyj SQLAlchemy ORM do stworzenia modeli
#    - Dodaj pola `id` jeżeli są potrzebne
#    - Możesz użyć dowolnego modułu z biblioteki standardowej
#    - Możesz użyć SQLAlchemy i Alembic
#    - Nie instaluj ani nie używaj dodatkowych pakietów

# %% Result
