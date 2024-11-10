"""
* Assignment: Accessor Descriptor ValueRange
* Complexity: medium
* Lines of code: 9 lines
* Time: 13 min

English:
    1. Define descriptor class `ValueRange` with attributes:
        a. `name: str`
        b. `min: float`
        c. `max: float`
    2. Define class `User` with attributes:
        a. `firstname: str`
        b. `lastname: str`
        c. `age: int` range from 18 to 65
        d. `height: float` range from 150 to 200
        e. `weight: float` range from 50 to 150
    3. Setting `User` attribute should invoke boundary check
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę-deskryptor `ValueRange` z atrybutami:
        a. `name: str`
        b. `min: float`
        c. `max: float`
    2. Zdefiniuj klasę `User` z atrybutami:
        a. `firstname: str`
        b. `lastname: str`
        c. `age: int` zakres od 18 do 65
        d. `height: float` zakres od 150 do 200
        e. `weight: float` zakres od 50 do 150
    3. Ustawianie atrybutu `User` powinno wywołać sprawdzanie zakresu
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> mark = User('Mark', 'Watney', age=36, height=170, weight=80)

    >>> melissa = User('Melissa', 'Lewis', age=66, height=170, weight=80)
    Traceback (most recent call last):
    ValueError: age is not between 18 and 65

    >>> rick = User('Rick', 'Martinez', age=39, height=201, weight=75)
    Traceback (most recent call last):
    ValueError: height is not between 150 and 200

    >>> alex = User('Alex', 'Vogel', age=41, height=175, weight=151)
    Traceback (most recent call last):
    ValueError: weight is not between 50 and 150
"""


# Define descriptor class `ValueRange` with attributes:
# - `name: str`
# - `min: float`
# - `max: float`
class ValueRange:
    name: str
    min: float
    max: float

# Define class `User` with attributes:
# - `firstname: str`
# - `lastname: str`
# - `age: int` range from 18 to 65
# - `height: float` range from 150 to 200
# - `weight: float` range from 50 to 150
#
# Setting `User` attribute should invoke boundary check
class User:
    firstname: str
    lastname: str
    age: int
    height: float
    weight: float

    def __init__(self, firstname, lastname, age, height, weight):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.height = height
        self.weight = weight


