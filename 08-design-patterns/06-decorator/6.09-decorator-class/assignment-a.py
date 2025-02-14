"""
Name: Decorator Class Syntax
Difficulty: easy
Lines: 5
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isclass

>>> assert isclass(MyDecorator), \
'MyDecorator should be a decorator class'

>>> assert MyDecorator(lambda: ...), \
'MyDecorator should take function as an argument'

>>> assert isinstance(MyDecorator(lambda: ...), MyDecorator), \
'MyDecorator() should return an object which is an instance of MyDecorator'

>>> @MyDecorator
... def echo(text):
...     return text

>>> echo('hello')
'hello'

"""

# %% SetUp

MyDecorator: type

# English
# 1. Create decorator class `MyDecorator`
# 2. `MyDecorator` should have `__init__` which takes function as an argument
# 3. `MyDecorator` should have `__call__` with parameters: `*args` and `**kwargs`
# 4. `__call__` should call original function with original parameters, and return its value
# 5. Run doctests - all must succeed

# Polish
# 1. Stwórz dekorator klasę `MyDecorator`
# 2. `MyDecorator` powinien mieć `__init__`, który przyjmuje funkcję jako argument
# 3. `MyDecorator` powinien mieć `__call__` z parameterami: `*args` i `**kwargs`
# 4. `__call__` powinien wywoływać oryginalną funkcję oryginalnymi parametrami i zwracać jej wartość
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
