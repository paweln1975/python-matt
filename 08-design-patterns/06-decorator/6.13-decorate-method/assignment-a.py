"""
Name: Decorator Method Syntax
Difficulty: easy
Lines: 5
Minutes: 3

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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isfunction

>>> assert isfunction(mydecorator), \
'Create mydecorator() function'

>>> assert isfunction(mydecorator(lambda: ...)), \
'mydecorator() should take method as an argument'

>>> class MyClass:
...     @mydecorator
...     def echo(self, text):
...         return text

>>> my = MyClass()
>>> my.echo('hello')
'hello'

"""

# %% SetUp

from typing import Callable
mydecorator: Callable[[Callable], Callable]

# English
# 1. Create method decorator `mydecorator`
# 2. Decorator should have `wrapper` with `*args` and `**kwargs` parameters
# 3. Wrapper should call original method with it's original parameters,
#    and return its value
# 4. Decorator should return `wrapper` method
# 5. Run doctests - all must succeed

# Polish
# 1. Stwórz dekorator metod `mydecorator`
# 2. Dekorator powinien mieć `wrapper` z parametrami `*args` i `**kwargs`
# 3. Wrapper powinien wywoływać oryginalną funkcję z jej oryginalnymi
#    parametrami i zwracać jej wartość
# 4. Decorator powinien zwracać metodę `wrapper`
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
