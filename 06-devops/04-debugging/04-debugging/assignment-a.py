"""
* Assignment: Own `doctest`
* Complexity: easy
* Lines of code: 60 lines
* Time: 21 min

English:
    1. For code from listing
    2. Write your own simplified implementation of `doctest`
    3. For simplicity, assume that only one line will always be returned (directly below the test)
    4. Run doctests - all must succeed

Polish:
    1. Dla kodu z listingu
    2. Napisz własną uproszczoną implementację `doctest`
    3. Dla uproszczenia przyjmij, że zwracana zawsze będzie tylko jedna linia (bezpośrednio poniżej testu)
    4. Uruchom doctesty - wszystkie muszą się powieść
"""

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


