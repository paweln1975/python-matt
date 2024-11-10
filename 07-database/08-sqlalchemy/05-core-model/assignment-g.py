
"""
* Assignment: Model Data DatabaseDump
* Complexity: medium
* Lines of code: 13 lines
* Time: 13 min

English:
    1. You received input data in JSON format from the API
       a. `str` fields: firstname, lastname, role, username, password, email,
       b. `datetime` fields: birthdate, last_login,
       c. `bool` fields: is_active, is_staff, is_superuser,
       d. `list[dict]` field: user_permissions
    2. Using `dataclass` model data as class `User`
       a. Note, that fields order is important for tests to pass
    3. Do not create additional classes to represent `permission` filed,
       leave it as `list[dict]`
    4. Non-functional requirements:
        a. Use SQLAlchemy ORM to create models
        b. Do not convert data, just model it
        c. You can use any Python standard library module
        d. You can use SQLAlchemy and Alembic
        e. Do not install or use 3rd party modules
    5. Run doctests - all must succeed

Polish:
    1. Otrzymałeś z API dane wejściowe w formacie JSON
       a. pola `str`: firstname, lastname, role, username, password, email,
       b. pola `datetime`: birthdate, last_login,
       c. pola `bool`: is_active, is_staff, is_superuser,
       d. pola `list[dict]`: user_permissions
    2. Wykorzystując `dataclass` zamodeluj dane za pomocą klasy `User`
       a. Zwróć uwagę, że kolejność pól ma znaczenie aby testy przechodziły
    3. Nie twórz dodatkowych klas do reprezentacji pola `permission`,
       niech zostanie jako `list[dict]`
    4. Wymagania niefunkcjonalne:
        a. Użyj SQLAlchemy ORM do stworzenia modeli
        b. Nie konwertuj danych, tylko je zamodeluj
        c. Możesz użyć dowolnego modułu z biblioteki standardowej
        d. Możesz użyć SQLAlchemy i Alembic
        e. Nie instaluj ani nie używaj dodatkowych pakietów
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass
    >>> from dataclasses import is_dataclass
    >>> from pprint import pprint

    >>> assert isclass(User)
    >>> assert is_dataclass(User)

    >>> attributes = User.__dataclass_fields__.keys()
    >>> list(attributes)  # doctest: +NORMALIZE_WHITESPACE
    ['firstname', 'lastname', 'role', 'username', 'password', 'email',
     'birthdate', 'last_login', 'is_active', 'is_staff', 'is_superuser',
     'user_permissions']

    >>> result = [User(**user['fields']) for user in json.loads(DATA)]

    >>> pprint(result[0])  # doctest: +ELLIPSIS
    User(firstname='Melissa',
         lastname='Lewis',
         role='commander',
         username='mlewis',
         password='pbkdf2_sha256$120000$gvEBNiCeTrYa0$5C+NiCeTrYsha1PHog...=',
         email='mlewis@nasa.gov',
         birthdate='1995-07-15',
         last_login='1970-01-01T00:00:00.000+00:00',
         is_active=True,
         is_staff=True,
         is_superuser=False,
         user_permissions=[{'eclss': ['add', 'modify', 'view']},
                           {'communication': ['add', 'modify', 'view']},
                           {'medical': ['add', 'modify', 'view']},
                           {'science': ['add', 'modify', 'view']}])
"""

import json
from dataclasses import dataclass
from datetime import date, datetime


DATA = ('[{"model":"authorization.user","pk":1,"fields":{"firstname":"Meli'
        'ssa","lastname":"Lewis","role":"commander","username":"mlewis","p'
        'assword":"pbkdf2_sha256$120000$gvEBNiCeTrYa0$5C+NiCeTrYsha1PHogqv'
        'XNiCeTrY0CRSLYYAA90=","email":"mlewis@nasa.gov","birthdate":"1995-'
        '07-15","last_login":"1970-01-01T00:00:00.000+00:00","is_active":t'
        'rue,"is_staff":true,"is_superuser":false,"user_permissions":[{"ec'
        'lss":["add","modify","view"]},{"communication":["add","modify","v'
        'iew"]},{"medical":["add","modify","view"]},{"science":["add","mod'
        'ify","view"]}]}},{"model":"authorization.user","pk":2,"fields":{"'
        'firstname":"Rick","lastname":"Martinez","role":"pilot","username"'
        ':"rmartinez","password":"pbkdf2_sha256$120000$aXNiCeTrY$UfCJrBh/q'
        'hXohNiCeTrYH8nsdANiCeTrYnShs9M/c=","birthdate":"1996-01-21","last_'
        'login":null,"email":"rmartinez@nasa.gov","is_active":true,"is_sta'
        'ff":true,"is_superuser":false,"user_permissions":[{"communication'
        '":["add","view"]},{"eclss":["add","modify","view"]},{"science":["'
        'add","modify","view"]}]}},{"model":"authorization.user","pk":3,"f'
        'ields":{"firstname":"Alex","lastname":"Vogel","role":"chemist","u'
        'sername":"avogel","password":"pbkdf2_sha256$120000$eUNiCeTrYHoh$X'
        '32NiCeTrYZOWFdBcVT1l3NiCeTrY4WJVhr+cKg=","email":"avogel@esa.int"'
        ',"birthdate":"1994-11-15","last_login":null,"is_active":true,"is_s'
        'taff":true,"is_superuser":false,"user_permissions":[{"eclss":["ad'
        'd","modify","view"]},{"communication":["add","modify","view"]},{"'
        'medical":["add","modify","view"]},{"science":["add","modify","vie'
        'w"]}]}},{"model":"authorization.user","pk":4,"fields":{"firstname'
        '":"Chris","lastname":"Beck","role":"crew-medical-officer","userna'
        'me":"cbeck","password":"pbkdf2_sha256$120000$3G0RNiCeTrYlaV1$mVb6'
        '2WNiCeTrYQ9aYzTsSh74NiCeTrY2+c9/M=","email":"cbeck@nasa.gov","bir'
        'thdate":"1999-08-02","last_login":"1970-01-01T00:00:00.000+00:00",'
        '"is_active":true,"is_staff":true,"is_superuser":false,"user_permi'
        'ssions":[{"communication":["add","view"]},{"medical":["add","modi'
        'fy","view"]},{"science":["add","modify","view"]}]}},{"model":"aut'
        'horization.user","pk":5,"fields":{"firstname":"Beth","lastname":"'
        'Johanssen","role":"sysop","username":"bjohanssen","password":"pbk'
        'df2_sha256$120000$QmSNiCeTrYBv$Nt1jhVyacNiCeTrYSuKzJ//WdyjlNiCeTr'
        'YYZ3sB1r0g=","email":"bjohanssen@nasa.gov","birthdate":"2006-05-09'
        '","last_login":null,"is_active":true,"is_staff":true,"is_superuse'
        'r":false,"user_permissions":[{"communication":["add","view"]},{"s'
        'cience":["add","modify","view"]}]}},{"model":"authorization.user"'
        ',"pk":6,"fields":{"firstname":"Mark","lastname":"Watney","role":"'
        'botanist","username":"mwatney","password":"pbkdf2_sha256$120000$b'
        'xS4dNiCeTrY1n$Y8NiCeTrYRMa5bNJhTFjNiCeTrYp5swZni2RQbs=","email":"'
        'mwatney@nasa.gov","birthdate":"1994-10-12","last_login":null,"is_a'
        'ctive":true,"is_staff":true,"is_superuser":false,"user_permission'
        's":[{"communication":["add","modify","view"]},{"science":["add","'
        'modify","view"]}]}}]')

# Using `dataclass` model data as class `User`
# type: type
class User:
    ...


