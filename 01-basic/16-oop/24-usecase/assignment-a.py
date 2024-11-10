"""
* Assignment: OOP Usecase Calculator
* Type: class assignment
* Complexity: easy
* Lines of code: 13 lines
* Time: 5 min

English:
    1. Define class `Calculator` with methods:
        a. `__init__()` takes two arguments `a` and `b` and sets them as fields
        b. `add()` which returns sum of `a` and `b`
        c. `sub()` which returns difference of `a` and `b`
        d. `mul()` which returns product of `a` and `b`
        e. `div()` which returns division of `a` and `b`
        f. `mean()` which returns arithemetic average of `a` and `b`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Calculator` z metodami:
        a. `__init__()` przyjmuje dwa argumenty `a` i `b` i ustawia je jako pola
        b. `add()` która zwraca sumę `a` i `b`
        c. `sub()` która zwraca różnicę `a` i `b`
        d. `mul()` która zwraca iloczyn `a` i `b`
        e. `div()` która zwraca iloraz `a` i `b`
        f. `mean()` która zwraca średnią arytmetyczną `a` i `b`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(Calculator)
    >>> calc = Calculator(1, 2)

    >>> assert ismethod(calc.add)
    >>> assert ismethod(calc.sub)
    >>> assert ismethod(calc.mul)
    >>> assert ismethod(calc.div)
    >>> assert ismethod(calc.mean)

    >>> calc.add()
    3
    >>> calc.sub()
    -1
    >>> calc.mul()
    2
    >>> calc.div()
    0.5
    >>> calc.mean()
    1.5
"""

# Define class `Calculator` with methods:
# - `__init__()` takes two arguments `a` and `b` and sets them as fields
# - `add()` which returns sum of `a` and `b`
# - `sub()` which returns difference of `a` and `b`
# - `mul()` which returns product of `a` and `b`
# - `div()` which returns division of `a` and `b`
# - `mean()` which returns arithemetic average of `a` and `b`

class Calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b if self.b != 0 else None

    def mean(self):
        return (self.a + self.b) / 2
