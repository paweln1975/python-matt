"""
* Assignment: Operator String Str
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Modify class `Iris` to overwrite `__str__()` method
    2. While printing object show: species name and a sum of `self.values`,
       example: `species='setosa', total=9.4`
    3. Result of sum round to one decimal place
    4. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj klasę `Iris` aby nadpisać metodę `__str__()`
    2. Przy wypisywaniu obiektu pokaż: nazwę gatunku i sumę `self.values`,
       przykład: `species='setosa', total=9.4`
    3. Wynik sumowania zaokrąglij do jednego miejsca po przecinku
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * f'{var=:.1f}'

Tests:
    >>> import sys; sys.tracebacklimit = 0

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


class Iris:
    values: list
    species: str

    def __init__(self, values, species):
        self.values = values
        self.species = species

# Modify class `Iris` to overwrite `__str__()` method
# While printing object show: species name and a sum of `self.values`,
# example: `species='setosa', total=9.4`
# Result of sum round to one decimal place
    def __str__(self):
        ...


