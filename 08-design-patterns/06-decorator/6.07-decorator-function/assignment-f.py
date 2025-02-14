"""
Name: Decorator Function TypeCheck
Difficulty: hard
Lines: 15
Minutes: 21

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
Terminal: `python -m doctest -v assignment-f.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isfunction

>>> assert isfunction(typecheck), \
'Create typecheck() function'

>>> assert isfunction(typecheck(lambda: ...)), \
'typecheck() should take function as an argument'

>>> @typecheck
... def echo(a: str, b: int, c: float = 0.0) -> bool:
...     return bool(a * b)

>>> echo('one', 1)
True
>>> echo('one', 1, 1.1)
True
>>> echo('one', b=1)
True
>>> echo('one', 1, c=1.1)
True
>>> echo('one', b=1, c=1.1)
True
>>> echo(a='one', b=1, c=1.1)
True
>>> echo(c=1.1, b=1, a='one')
True
>>> echo(b=1, c=1.1, a='one')
True
>>> echo('one', c=1.1, b=1)
True
>>> echo(1, 1)
Traceback (most recent call last):
TypeError: "a" is <class 'int'>, but <class 'str'> was expected
>>> echo('one', 'two')
Traceback (most recent call last):
TypeError: "b" is <class 'str'>, but <class 'int'> was expected
>>> echo('one', 1, 'two')
Traceback (most recent call last):
TypeError: "c" is <class 'str'>, but <class 'float'> was expected
>>> echo(b='one', a='two')
Traceback (most recent call last):
TypeError: "b" is <class 'str'>, but <class 'int'> was expected
>>> echo('one', c=1.1, b=1.1)
Traceback (most recent call last):
TypeError: "b" is <class 'float'>, but <class 'int'> was expected

>>> @typecheck
... def echo(a: str, b: int, c: float = 0.0) -> bool:
...     return str(a * b)
>>>
>>> echo('one', 1, 1.1)
Traceback (most recent call last):
TypeError: "return" is <class 'str'>, but <class 'bool'> was expected

Hints:
https://docs.python.org/3/howto/annotations.html
`inspect.get_annotations()`
`function.__code__.co_varnames`
`dict(zip(...))`
`dict.items()`
`dict1 | dict2` - merging dicts

"""

# %% SetUp

from inspect import get_annotations

from typing import Callable
typecheck: Callable[[Callable], Callable]

# English
# 1. Modify decorator `typecheck`
# 2. Decorator checks types of all arguments (`*args` oraz `**kwargs`)
# 3. Decorator checks return type
# 4. When received type is not expected raise `TypeError` with:
#    - argument name
#    - actual type
#    - expected type
# 5. Run doctests - all must succeed

# Polish
# 1. Zmodyfikuj dekorator `typecheck`
# 2. Dekorator sprawdza typy wszystkich argumentów (`*args` oraz `**kwargs`)
# 3. Dekorator sprawdza typ zwracany
# 4. Gdy otrzymany typ nie jest równy oczekiwanemu podnieś `TypeError` z:
#    - nazwa argumentu
#    - aktualny typ
#    - oczekiwany typ
# 5. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def typecheck(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper