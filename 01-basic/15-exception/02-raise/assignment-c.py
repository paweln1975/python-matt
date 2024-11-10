"""
* Assignment: Exception Raise PermissionError
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Check username and password passed to a `login` function
    2. If `username` is 'mwatney' and `password` is 'Ares3'
       then print 'User login'
    3. If any value is other than mentioned, raise an exception
       PermissionError with message 'Invalid username and/or password'
    4. Non-functional requirements:
        a. Write solution inside `result` function
        b. Mind the indentation level
    5. Run doctests - all must succeed

Polish:
    1. Sprawdź username i password przekazane do funckji `login`
    2. Jeżeli username jest 'mwatney' i hasło jest 'Ares3'
       to wyświetl na ekranie napis 'User login'
    3. Jeżeli którakolwiek wartość jest inna, to podnieś wyjątek
       PermissionError z komunikatem 'Invalid username and/or password'
    4. Wymagania niefunkcjonalne:
        a. Rozwiązanie zapisz wewnątrz funkcji `result`
        b. Zwróć uwagę na poziom wcięć
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `not in`
    * `raise`
    * `if`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> login('mwatney', 'Ares3')
    User login

    >>> login('invalid', 'Ares3')
    Traceback (most recent call last):
    PermissionError: Invalid username and/or password

    >>> login('mwatney', 'invalid')
    Traceback (most recent call last):
    PermissionError: Invalid username and/or password

    >>> login('invalid', 'invalid')
    Traceback (most recent call last):
    PermissionError: Invalid username and/or password
"""

# Username must be 'mwatney'
# Password must be 'Ares3'
# If user and password are correct print 'User login'
# Else: raise an exception PermissionError with message 'Invalid username and/or password'
# type: Callable[[str,str], Exception|None]
def login(username, password):
    if username == 'mwatney' and password == 'Ares3':
        print('User login')
    else:
        raise PermissionError('Invalid username and/or password')



