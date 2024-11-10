"""
* Assignment: DesignPatterns Creational PrototypeDragon
* Complexity: easy
* Lines of code: 6 lines
* Time: 8 min

English:
    1. Create class `Dragon`
    2. Dragon has attributes:
        a. `name: str`
        b. `position: tuple[int,int]` default `(0, 0)`
        c. `health: int` random from 50 to 100
        d. `gold: int` random from 1 to 100
        e. method `.clone()`
    3. Method `.clone()` returns another `Dragon` with the same values
    4. Use `random.randint()` to generate pseudorandom numbers
    5. Run doctests - all must succeed

Polish:
    1. Stwórz klasę `Dragon`
    2. Dragon ma atrybuty:
        a. `name: str`
        b. `position: tuple[int,int]` domyślnie `(0, 0)`
        c. `health: int` losowe od 50 do 100
        d. `gold: int` losowe od 1 do 100
        e. metodę `.clone()`
    3. Metoda `.clone()` zwraca kolejnego `Dragon` z tymi samymi wartościami
    4. Użyj `random.randint()` do generowania pseudolosowych liczb
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from random import seed
    >>> seed(0)

    >>> dragon = Dragon('Wawelski')
    >>> result = dragon.clone()

    >>> result.name
    'Wawelski'

    >>> result.health
    74

    >>> result.gold
    98

    >>> result.position
    (0, 0)
"""
from dataclasses import dataclass, field
from random import randint


@dataclass
class Dragon:
    ...


