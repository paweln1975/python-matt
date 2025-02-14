"""
Name: Own `doctest`
Difficulty: easy
Lines: 60
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:

"""

# %% SetUp

from typing import Callable
Astronaut: type
doctest: Callable[[str], None]

class Astronaut:
    """
    New Astronaut
    """

    def __init__(self, name):
        self.name = name

    def say_hello(self, lang='en'):
        """
        prints greeting according to the language

        >>> Astronaut(name='José Jiménez').say_hello(lang='es')
        '¡hola José Jiménez!'

        >>> Astronaut(name='Pan Twardowski').say_hello(lang='pl')
        'Witaj Pan Twardowski!'
        """
        if lang == 'en':
            return f'hello {self.name}'
        elif lang == 'es':
            return f'¡hola {self.name}!'
        elif lang == 'pl':
            return f'Witaj {self.name}!'
        else:
            return f'hello {self.name}!'

# English
# 1. For code from listing
# 2. Write your own simplified implementation of `doctest`
# 3. For simplicity, assume that only one line will always be returned (directly below the test)
# 4. Run doctests - all must succeed

# Polish
# 1. Dla kodu z listingu
# 2. Napisz własną uproszczoną implementację `doctest`
# 3. Dla uproszczenia przyjmij, że zwracana zawsze będzie tylko jedna linia (bezpośrednio poniżej testu)
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
