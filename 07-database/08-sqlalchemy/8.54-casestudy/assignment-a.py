"""
Name: Database Model Shop
Difficulty: medium
Lines: 50
Minutes: 55

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

>>> assert result_a is not Ellipsis, \
'Assign result to variable: `result_a`'
>>> assert type(result_a) is tuple, \
'Variable `result_a` has invalid type, should be tuple[str,str]'
>>> assert type(result_a[0]) is str, \
'Variable `result_a` has invalid type, should be tuple[str,str]'
>>> assert type(result_a[1]) is str, \
'Variable `result_a` has invalid type, should be tuple[str,str]'

>>> assert result_b is not Ellipsis, \
'Assign result to variable: `result_b`'
>>> assert type(result_b) is tuple, \
'Variable `result_b` has invalid type, should be tuple[str,str]'
>>> assert type(result_b[0]) is str, \
'Variable `result_b` has invalid type, should be tuple[str,str]'
>>> assert type(result_b[1]) is str, \
'Variable `result_b` has invalid type, should be tuple[str,str]'

>>> assert result_c is not Ellipsis, \
'Assign result to variable: `result_c`'
>>> assert type(result_c) is float, \
'Variable `result_c` has invalid type, should be float'

>>> assert result_d is not Ellipsis, \
'Assign result to variable: `result_d`'
>>> assert type(result_d) is str, \
'Variable `result_d` has invalid type, should be str'

>>> assert result_e is not Ellipsis, \
'Assign result to variable: `result_e`'
>>> assert type(result_e) is tuple, \
'Variable `result_e` has invalid type, should be tuple[float,str]'
>>> assert type(result_e[0]) is float, \
'Variable `result_e` has invalid type, should be tuple[float,str]'
>>> assert type(result_e[1]) is str, \
'Variable `result_e` has invalid type, should be tuple[float,str]'

>>> assert result_f is not Ellipsis, \
'Assign result to variable: `result_f`'
>>> assert type(result_f) is tuple, \
'Variable `result_f` has invalid type, should be tuple[float,str]'
>>> assert type(result_f[0]) is float, \
'Variable `result_f` has invalid type, should be tuple[float,str]'
>>> assert type(result_f[1]) is str, \
'Variable `result_f` has invalid type, should be tuple[float,str]'

"""

# %% SetUp

result_a: tuple[str,str]
result_b: tuple[str,str]
result_c: int
result_d: str
result_e: tuple[float,str]
result_f: tuple[float,str]

USERS = """firstname,lastname,birthdate,gender,ssn,email,phone
Mark,Watney,1994-10-12,male,94101212345,mwatney@nasa.gov,+1 (234) 555-0000
Melissa,Lewis,1995-07-15,female,95071512345,mlewis@nasa.gov,+1 (234) 555-0001
Rick,Martinez,1996-01-21,male,96012112345,rmartinez@nasa.gov,+1 (234) 555-0010
Alex,Vogel,1994-11-15,male,94111512345,avogel@esa.int,+49 (234) 555-0011
Beth,Johanssen,2006-05-09,female,06250912345,bjohanssen@nasa.gov,+1 (234) 555-0100
Chris,Beck,1999-08-02,male,99080212345,cbeck@nasa.gov,+1 (234) 555-0101"""

ADDRESSES = """user,type,street,city,postcode,region,country
mwatney@nasa.gov,billing,2101 E NASA Pkwy,Houston,77058,Texas,USA
mwatney@nasa.gov,shipment,,Kennedy Space Center,32899,Florida,USA
mlewis@nasa.gov,shipment,Kamienica Pod św. Janem Kapistranem,Kraków,31008,Małopolskie,Poland
rmartinez@nasa.gov,billing,,Звёздный городо́к,141160,Московская область,Россия
rmartinez@nasa.gov,shipment,,Космодро́м Байкону́р,,Кызылординская область,Қазақстан
avogel@esa.int,shipment,Linder Hoehe,Cologne,51147,North Rhine-Westphalia,Germany
bjohanssen@nasa.gov,shipment,2825 E Ave P,Palmdale,93550,California,USA
cbeck@nasa.gov,shipment,4800 Oak Grove Dr,Pasadena,91109,California,USA"""

PRODUCTS = """ean13,name,price
5039271113244,Alfa,123.00
5202038482222,Bravo,312.22
5308443764554,Charlie,812.00
5439667086587,Delta,332.18
5527865721147,Echo,114.00
5535686226512,Foxtrot,99.12
5721668602638,Golf,123.00
5776136485596,Hotel,444.40
5863969679442,India,674.21
5908105406923,Juliet,324.00
5957751061635,Kilo,932.20
6190780033092,Lima,128.00
6512625994397,Mike,91.00
6518235371269,November,12.00
6565923118590,Oscar,43.10
6650630136545,Papa,112.00
6692669560199,Quebec,997.10
6711341590108,Romeo,1337.00
6816011714454,Sierra,998.10
7050114819954,Tango,123.00
7251625012784,Uniform,564.99
7251925199277,Victor,990.50
7283004100423,Whisky,881.89
7309682004683,X-Ray,123.63
7324670042560,Zulu,311.00"""

ORDERS = """user,product
mwatney@nasa.gov,Sierra
mwatney@nasa.gov,Victor
bjohanssen@nasa.gov,Delta
mlewis@nasa.gov,November
rmartinez@nasa.gov,Mike
mwatney@nasa.gov,Bravo
mwatney@nasa.gov,Kilo
avogel@esa.int,Victor
bjohanssen@nasa.gov,Romeo
bjohanssen@nasa.gov,Whisky
cbeck@nasa.gov,Zulu
mwatney@nasa.gov,Romeo
avogel@esa.int,Romeo
bjohanssen@nasa.gov,Victor
bjohanssen@nasa.gov,Whisky
mlewis@nasa.gov,Whisky
rmartinez@nasa.gov,Mike
mwatney@nasa.gov,November
mwatney@nasa.gov,Kilo
avogel@esa.int,Bravo
bjohanssen@nasa.gov,X-Ray
avogel@esa.int,Romeo
bjohanssen@nasa.gov,Victor
bjohanssen@nasa.gov,India
mlewis@nasa.gov,Juliet
rmartinez@nasa.gov,Foxtrot
avogel@esa.int,Victor
bjohanssen@nasa.gov,Romeo
bjohanssen@nasa.gov,Whisky
cbeck@nasa.gov,Zulu
mwatney@nasa.gov,Alfa
avogel@esa.int,Romeo
bjohanssen@nasa.gov,Quebec"""

# English
# 1. Create model `User` with fields:
#    - firstname - first name
#    - lastname - last name
#    - birthdate - date of birth
#    - ssn - PESEL
#    - email - email address
#    - phone - phone with country code
# 2. Create model `Address` with fields:
#    - type - type of address: billing, shipment
#    - street - street, house number, apartment number
#    - postcode - postal code
#    - city - city
#    - region - province or state
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
#    - User can have one billing and one shipment address
#    - Address can have no street or postal code
#    - User can buy many products
#    - Product could not be purchased
# 6. Non-functional requirements:
#    - Add `id` fields if needed
#    - You can use any module from standard library
#    - You can use SQLAlchemy and Alembic
#    - Do not install or use additional packages
# 7. Display data that answers the questions:
#    - First and last name of the person who made the most purchases?
#    - First and last name of the person who made purchases for the largest amount?

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
#    - Dodaj pola `id` jeżeli są potrzebne
#    - Możesz użyć dowolnego modułu z biblioteki standardowej
#    - Możesz użyć SQLAlchemy i Alembic
#    - Nie instaluj ani nie używaj dodatkowych pakietów
# 7. Wyświetl dane odpowiadające na pytania:
#    - Imię i nazwisko osoby, która dokonała najwięcej zakupów?
#    - Imię i nazwisko osoby, która dokonała zakupów za największą kwotę?
#    - Kwota, za jaką łącznie dokonały zamówień kobiety?
#    - Nazwa produktu, który był najczęściej kupowany?
#    - Kwota i nazwa kraju, którego obywatele dokonali najwięcej zakupów?
#    - Kwota i nazwa kraju, którego obywatele dokonali zakupów za największą kwotę?

# %% Result
result_a = ...
result_b = ...
result_c = ...
result_d = ...
result_e = ...
result_f = ...