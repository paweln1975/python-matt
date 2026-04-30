# Dragon Game

## Setup

```pycon
>>> from dragon import Dragon
>>> from random import seed; seed(0)  # Set the seed for reproducibility

```

## Create a dragon

* When creating dragon has a name
* Dragon raises an error if name is not provided
* Dragon raises an error if name is provided as positional argument

Create a dragon:
```pycon
>>> dragon = Dragon("Wawelski")
>>> dragon.name
'Wawelski'

```
Dragon raises an error if name is not provided:
```pycon
>>> dragon = Dragon()
Traceback (most recent call last):
TypeError: Dragon.__init__() missing 1 required positional argument: 'name'

```

Dragon raises an error if name is provided as positional argument:
```pycon
>>> dragon = Dragon(name="Wawelski")
Traceback (most recent call last):
TypeError: Dragon.__init__() got some positional-only arguments passed as keyword arguments: 'name'

```

## Health of the dragon
* Dragon has health of random value between 50 and 100 (inclusively) when created
* Dragon may take damage
* Dragon dies when health drops to 0
* When dies health is set to 0, not negative

```pycon
>>> dragon = Dragon("Wawelski")
>>> 50 <= dragon.health <= 100
True

```

* To get the health of the dragon, use `health` property
```pycon
>>> dragon = Dragon("Wawelski")
>>> dragon.health
76

```

* Dragon takes damage with `take_damage` method
```pycon
>>> dragon = Dragon("Wawelski")
>>> dragon.take_damage(20)
>>> dragon.health
32

```

* Dragon dies when health drops to 0
* To check if the dragon is dead, use `is_dead` method
```pycon
>>> dragon = Dragon("Wawelski")
>>> dragon.take_damage(150)
>>> dragon.health
0

>>> dragon.is_dead()
True

```

## Position of the dragon
* Dragon has a position represented as a tuple of (x, y) coordinates
* Dragon can move to a new position with `move` method
* Move method takes combination of four positional arguments representing directions: up, down, left, right and number of steps to move in that direction
* Dragon can be moved in multiple directions at once
* Dragon's position is updated after moving
* Default position of the dragon is (0, 0), this is top-left corner of the coordinate system
* Dragon can only move if it is alive
* Dragon raises an error if trying to move when it is dead
* X coordinate increases when moving right and decreases when moving left
* Y coordinate increases when moving down and decreases when moving up

To set initial dragon position use positional arguments in the constructor:

```pycon
>>> dragon = Dragon("Wawelski", pos_x=10, pos_y=20)

```

To get dragon position:

```pycon
>>> dragon = Dragon("Wawelski", pos_x=10, pos_y=20)
>>> dragon.get_position()
(10, 20)

```

If dragon position is not set in the constructor, it defaults to (0, 0):

```pycon
>>> dragon = Dragon("Wawelski")
>>> dragon.get_position()
(0, 0)

```

To set dragon position (as positional arguments, if not given, default is 0 for both x and y):

```pycon
>>> dragon = Dragon("Wawelski")
>>> dragon.set_position(pos_x=5, pos_y=10)
>>> dragon.get_position()
(5, 10)

```

```pycon
>>> dragon = Dragon("Wawelski")
>>> dragon.set_position(pos_x=5)
>>> dragon.get_position()
(5, 0)

```

```pycon
>>> dragon = Dragon("Wawelski")
>>> dragon.set_position(pos_y=5)
>>> dragon.get_position()
(0, 5)

```

To move the dragon:

```pycon
>>> dragon = Dragon("Wawelski")
>>> dragon.move(down=2, right=3)
>>> dragon.get_position()
(3, 2)

```
If the dragon is dead, it cannot moved:

```pycon
>>> dragon = Dragon("Wawelski")
>>> dragon.take_damage(150)
>>> dragon.move(down=2, right=3)
Traceback (most recent call last):
ValueError: Cannot move a dead dragon

```

Move the dragon in multiple directions at once:

```pycon
>>> dragon = Dragon("Wawelski")
>>> dragon.move(up=1, left=2, down=3, right=4)
>>> dragon.get_position()
(2, 2)

```

## Damage
* Dragon makes random damage between 5 and 20 (inclusively) when attacking

To make damage from the dragon, use `make_damage` method:

```pycon
>>> dragon = Dragon("Wawelski")
>>> dmg = dragon.make_damage()
>>> 5 <= dmg <= 20
True

```

```pycon
>>> dragon = Dragon("Wawelski")
>>> dmg = dragon.make_damage()
>>> dmg
9

```

