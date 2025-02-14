"""
Name: DesignPatterns Creational BuilderTexture
Difficulty: easy
Lines: 18
Minutes: 5

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-e.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from pprint import pprint

>>> result = (
...     Texture()
...     .with_file('img/dragon/alive.png')
...     .with_height(100)
...     .with_width(50)
...     .with_quality(75)
... )

>>> vars(result)
{'file': 'img/dragon/alive.png', 'height': 100, 'width': 50, 'quality': 75}

"""

# %% SetUp

from typing import Callable

Texture: type
with_file: Callable[[object, str], object]
with_width: Callable[[object, int], object]
with_height: Callable[[object, int], object]
with_quality: Callable[[object, int], object]

# English
# 1. Create class `Texture`
# 2. Use builder pattern to set:
#    - `file: str`
#    - `width: int` value greater than 0
#    - `height: int` value greater than 0
#    - `quality: int` from 1 to 100 percent
# 3. Run doctests - all must succeed

# Polish
# 1. Stwórz klasę `Texture`
# 2. Użyj wzorca builder, aby ustawić:
#    - `file: str`
#    - `width: int` wartość większa niż 0
#    - `height: int` wartość większa niż 0
#    - `quality: int` od 1 do 100 procent
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Texture:
    file: str
    width: int
    height: int
    quality: int