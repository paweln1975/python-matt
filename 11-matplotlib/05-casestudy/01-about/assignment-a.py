
"""
* Assignment: Trigonometry
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    ...

Polish:
    1. Dla `x` z przedziału od 0.0 do 1.0 z próbkowaniem co 0.01 przedstaw przebiegi funkcji `sin`, `cos` dla parametrów `2 * np.pi * x`
    2. Stwórz dwa osobne obrazki (figure):
        a. Każdy z przebiegów na osobnym subplot
        b. Na jednym plot dwa przebiegi funkcji
    3. Wykresy (`subplot`) mają być jeden nad drugim
    4. Wykresy podpisz nazwą funkcji trygonometrycznej
    5. Tekst etykiety osi `y` ustaw na "Wartość funkcji"
    6. Pokoloruj nazwy tików `x` dla wykresu `sin` na czerwono
    7. Pokoloruj nazwę (label) dla `cos` na kolor zielony
    8. Na obu wykresach pokaż grid
    9. Narysuj drugi obrazek z nałożonymi na jeden plot wykresami obu funkcji
    10. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `np.sin()`
    * `np.cos()`
"""

import matplotlib.pyplot as plt
import numpy as np


