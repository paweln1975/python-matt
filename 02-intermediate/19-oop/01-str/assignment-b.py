
# region Show Doctests
"""
Doctests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> iris = Iris(
...     values=[4.7, 3.2, 1.3, 0.2],
...     species='setosa',
... )
>>> print(iris)
species='setosa', total=9.4

>>> iris = Iris(
...     values=[7.0, 3.2, 4.7, 1.4],
...     species='versicolor',
... )
>>> print(iris)
species='versicolor', total=16.3
"""
# endregion

# region Show Types
from typing import Callable
Iris: type
__str__: Callable[[object], str]
# endregion

# English
# 1. Modify class `Iris` to overwrite `__str__()` method
# 2. While printing object show: species name and a sum of `self.values`,
#    example: `species='setosa', total=9.4`
# 3. Result of sum round to one decimal place
# 4. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj klasę `Iris` aby nadpisać metodę `__str__()`
# 2. Przy wypisywaniu obiektu pokaż: nazwę gatunku i sumę `self.values`,
#    przykład: `species='setosa', total=9.4`
# 3. Wynik sumowania zaokrąglij do jednego miejsca po przecinku
# 4. Uruchom doctesty - wszystkie muszą się powieść

# region Show Hints
# - `f'{var=:.1f}'`
# endregion

# %% Your code
class Iris:
    values: list
    species: str

    def __init__(self, values, species):
        self.values = values
        self.species = species

    def __str__(self):
        total = sum(self.values)
        return f"species='{self.species}', total={total}"
