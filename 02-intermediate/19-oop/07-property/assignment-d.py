
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert hasattr(Iris, 'mean')
>>> assert hasattr(Iris, 'sum')
>>> assert hasattr(Iris, 'len')

>>> from inspect import isfunction
>>> assert isfunction(Iris.mean)
>>> assert isfunction(Iris.sum)
>>> assert isfunction(Iris.len)

>>> result = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')
>>> result.len()
4
>>> result.sum()
10.2
>>> result.mean()
2.55
"""
# endregion

# region Show Types
from typing import Callable
Iris: type
sum: Callable[[object], float]
len: Callable[[object], int]
mean: Callable[[object], float]
# endregion

# English
# 1. Modify class `Iris`
# 2. Implement methods:
#    - `Iris.sum()` - returning sum of numeric attributes
#    - `Iris.len()` - returning number of numeric attributes
#    - `Iris.mean()` - returning mean of numeric attributes
# 3. Use property `Iris.numeric_values`
# 4. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `Iris`
# 2. Zaimplementuj metody:
#    - `Iris.sum()` - zwracającą sumę numerycznych atrybutów
#    - `Iris.len()` - zwracającą liczbę numerycznych atrybutów
#    - `Iris.mean()` - zwracającą średnią numerycznych atrybutów
# 3. Użyj property `Iris.numeric_values`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# region Show Hints
# - `sum()`
# - `len()`
# - `sum() / len()`
# endregion

# %% Your code
class Iris:
    def __init__(self, sl, sw, pl, pw, species):
        self.sepal_length = sl
        self.sepal_width = sw
        self.petal_length = pl
        self.petal_width = pw
        self.species = species

    @property
    def numeric_values(self):
        return tuple(x for x in vars(self).values() if type(x) is float)

    def sum(self):
        return sum(self.numeric_values)

    def len(self):
        return len(self.numeric_values)

    def mean(self):
        return self.sum() / self.len()
