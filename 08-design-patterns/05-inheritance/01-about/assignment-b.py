"""
* Assignment: Inheritance About Single
* Complexity: easy
* Lines of code: 8 lines
* Time: 3 min

English:
    1. Define class `Account`
    2. Define classe `User` inheriting from `Account`
    3. Define classe `Admin` inheriting from `Account`
    4. Use single inheritance
    5. Assignment demonstrates syntax, so do not add any attributes and methods
    6. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Account`
    2. Zdefiniuj klasę `User` dziedziczacą po `Account`
    3. Zdefiniuj klasę `Admin` dziedziczacą po `Account`
    4. Użyj pojedynczego dziedziczenia
    5. Zadanie demonstruje składnię, nie dodawaj żadnych atrybutów i metod
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Account)
    >>> assert isclass(User)
    >>> assert isclass(Admin)

    >>> assert issubclass(User, Account)
    >>> assert issubclass(Admin, Account)

    >>> assert len(Account.__subclasses__()) == 2
    >>> assert len(User.__subclasses__()) == 0
    >>> assert len(Admin.__subclasses__()) == 0
"""

# Define class `Account`
...

# Define classe `User` inheriting from `Account`
...

# Define classe `Admin` inheriting from `Account`
...

