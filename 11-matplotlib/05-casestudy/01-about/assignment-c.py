"""
* Assignment: Random Points
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    1. Generate 100 random points:
        a. gaussian distribution with mean 0
        b. standard deviation equal to 0.2
    2. Points must be generated around two selected points (`A = (0, 1)`, `B = (2, 4)`).
    3. Function must pass `doctest`
    4. Draw these points on the chart (you can use the `plt.axis('equal')` function to make the axes of the chart in the same scale).
    5. Point A and points generated on its basis draw in red
    6. point B and points generated on its basis draw in blue
    7. You can write a function for this purpose `plot_point(point, color)`, which takes a point (two-element tuple or list, of which the first element is the x coordinate and the second is y), and color and adds this point to the currently active drawing.
    8. Using the function written in the exercise above, calculate the distance from each of the points to points A and B
    9. Based on this distance, classify these points
        a. if the point is closer to point A, it belongs to the A set
        b. if it is closer to the B set, it belongs to the B set
    10. Draw a new chart on which:
        a. points from the A set will be drawn in red,
        b. points from the B set will be drawn in blue.
    11. Are two charts the same?
    12. What happens if we increase the standard deviation when generating points?
    13. Or we will approximate points A and B to each other?
    14. Run doctests - all must succeed

Polish:
    1. Wygeneruj 100 losowych punktów:
        a. rozkład gaussa o średniej 0
        b. o odchyleniu standardowym równym 0.2
    2. Punkty muszą być wylosowane wokół dwóch wybranych punktów (`A = (0, 1)`, `B = (2, 4)`).
    3. Funkcja musi przechodzić `doctest`
    4. Wyrysuj te punkty na wykresie (możesz użyć funkcji `plt.axis('equal')` żeby osie wykresu były w tej samej skali).
    5. Punkt A i punkty wygenerowane na jego podstawie wyrysuj kolorem czerwonym
    6. punkt B i punkty wygenerowane na jego podstawie wyrysuj kolorem niebieskim
    7. Możesz do tego celu napisać funkcję `plot_point(point, color)`, która przyjmuje punkt (dwuelementowy tuple, lub listę, z czego pierwszy element to współrzędna x, a druga to y), i kolor i doda ten punkt do aktualnie aktywnego rysunku.
    8. Korzystając z funkcji napisanej w ćwiczeniu powyżej oblicz odległość od każdego z punktów do punktów A i B
    9. Na podstawie tej odległości zaklasyfikuj te punkty
        a. jeżeli punkt jest bliżej punktu A to należy do zbioru A
        b. jeżeli jest bliżej do zbioru B to należy do zbioru B
    10. Narysuj nowy wykres, na którym:
        a. punkty ze zbioru A będą narysowane kolorem czerwonym,
        b. punkty ze zbioru B będą narysowane kolorem niebieskim.
    11. Czy dwa wykresy są takie same?
    12. Co się stanie jeżeli będziemy zwiększali odchylenie standardowe przy generacji punktów?
    13. Albo przybliżymy do siebie punkty A i B?
    14. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * argument `color='red'` w funkcji `plt.plot`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> import numpy as np
    >>> np.random.seed(0)

    >>> result((0,0), std=0.2)  # doctest: +SKIP
    (0.2576369506310926, 0.2898891217399542)

    >>> result((0,0))  # doctest: +SKIP
    (0.2576369506310926, 0.2898891217399542)

    >>> result((2,5), std=10)  # doctest: +SKIP
    (14.881847531554628, 19.494456086997708)

    >>> result((2,5), std=(0.1, 12))  # doctest: +SKIP
    (2.1288184753155464, 22.393347304397253)

   
"""


