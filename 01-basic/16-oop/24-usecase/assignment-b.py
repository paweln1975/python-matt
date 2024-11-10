"""
* Assignment: OOP Usecase Dragon
* Type: class assignment
* Complexity: easy
* Lines of code: 13 lines
* Time: 21 min

English:
    1. Define class `Dragon` with methods
    2. Define method `__init__()` takes arguments three arguments:
       `name`, `position_x` and `position_y` and sets them as fields
    3. Define method `set_position()` which takes `x` and `y`
       and sets `position_x` and `position_y`
    4. Define method `get_position()` which returns
       a tuple with `position_x` and `position_y`
    5. Define method `move()` which takes four arguments
       `left`, `right`, `up`, `down`, all defauls to 0
       and changes `position_x` and `position_y` accordingly
    6. Top left corner is (0, 0):
       a. Moving up increases `position_y`
       b. Moving left decreases `position_x`
       c. Moving up increases `position_y`
       d. Moving down decreases `position_y`
    7. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Dragon`
    2. Zdefiniuj metodę `__init__()` przyjmującą trzy argumenty:
       `name`, `position_x` i `position_y` i ustawia je jako pola
    3. Zdefiniuj metodę `set_position()` która przyjmuje `x` i `y`
       i ustawia `position_x` i `position_y`
    4. Zdefiniuj metodę `get_position()` która zwraca
       krotkę z `position_x` i `position_y`
    5. Zdefiniuj metodę `move()` która przyjmuje cztery argumenty
       `left`, `right`, `up`, `down`, wszystkie domyślnie 0
       i zmienia `position_x` i `position_y` odpowiednio
    6. Lewy górny róg to (0, 0):
       a. Poruszanie w górę zwiększa `position_y`
       b. Poruszanie w lewo zmniejsza `position_x`
       c. Poruszanie w górę zwiększa `position_y`
       d. Poruszanie w dół zmniejsza `position_y`
    7. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass, ismethod

    >>> assert isclass(Dragon)

    >>> wawelski = Dragon('Wawelski', position_x=50, position_y=100)
    >>> wawelski.set_position(x=10, y=20)
    >>> wawelski.get_position()
    (10, 20)
    >>> wawelski.move(left=10, down=20)
    >>> wawelski.move(left=10, right=15)
    >>> wawelski.move(right=15, up=5)
    >>> wawelski.move(down=5)
    >>> wawelski.get_position()
    (20, 40)
"""

# Define class `Dragon` with methods:
# - `__init__()`
# - `set_position()`
# - `get_position()`
# - `move()`
#
# Top left corner is (0, 0):
# - Moving up increases `position_y`
# - Moving left decreases `position_x`
# - Moving up increases `position_y`
# - Moving down decreases `position_y`

# type: type
class Dragon():
    def __init__(self, name, position_x, position_y):
        self.x = position_x
        self.y = position_y
        self.name = name

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return (self.x, self.y)

    def move(self, left=0, right=0, up=0, down=0):
        self.y -= up
        self.y += down
        self.x -= left
        self.x += right

