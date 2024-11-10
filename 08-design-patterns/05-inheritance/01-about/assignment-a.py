"""
* Assignment: Inheritance About None
* Complexity: easy
* Lines of code: 8 lines
* Time: 3 min

English:
    1. Define classe `Account`
    2. Define classe `User`
    3. Define classe `Admin`
    4. Do not use inheritance
    5. Assignment demonstrates syntax, so do not add any attributes and methods
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Account`
    2. Zdefiniuj klasę `User`
    3. Zdefiniuj klasę `Admin`
    4. Nie używaj dziedziczenia
    5. Zadanie demonstruje składnię, nie dodawaj żadnych atrybutów i metod
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Account)
    >>> assert isclass(User)
    >>> assert isclass(Admin)

    >>> assert not issubclass(User, Account)
    >>> assert not issubclass(Admin, Account)

    >>> assert len(Account.__subclasses__()) == 0
    >>> assert len(User.__subclasses__()) == 0
    >>> assert len(Admin.__subclasses__()) == 0
"""

# Define classe `Account`
...

# Define classe `User`
...

# Define classe `Admin`
...

