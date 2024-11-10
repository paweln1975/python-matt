"""
* Assignment: Iterable Tuple Mean
* Type: class assignment
* Complexity: medium
* Lines of code: 8 lines
* Time: 8 min

English:
    1. Define variables:
        a. `result_a` with arithmetic mean of column `sepal_length`
        b. `result_b` with arithmetic mean of column `sepal_width`
        c. `result_c` with arithmetic mean of column `petal_length`
        d. `result_d` with arithmetic mean of column `petal_width`
    2. Use column selection with `alt` key shortcut
    3. Do not use `str.split()`, `slice`, `getitem`, `for`, `while`
       or any other control-flow statement
    4. Non-functional requirements:
        a. practice tuple creation syntax, not automation
        b. practice vertical selection in IDE
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienne:
        a. `result_a` z średnią arytmetyczną kolumny `sepal_length`
        b. `result_b` z średnią arytmetyczną kolumny `sepal_width`
        c. `result_c` z średnią arytmetyczną kolumny `petal_length`
        d. `result_d` z średnią arytmetyczną kolumny `petal_width`
    2. Wykorzystaj zaznaczanie kolumnowe za pomocą klawisza `alt`
    3. Nie używaj `str.split()`, `slice`, `getitem`, `for`, `while`
       lub jakiejkolwiek innej instrukcji sterującej
    4. Wymagania niefunkcjonalne:
        a. przećwicz składnię tworzenia `tuple`, a nie automatyzację,
        b. przećwicz zaznaczanie pionowe w IDE
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `mean = sum(...) / len(...)`
    * `ALT` + `left mouse button` = multiple select
    * `ALT` + `SHIFT` + `left mouse button drag` = vertical selection
    * `ALT` + `SHIFT` + `right` = select word to the right (macOS)
    * `ALT` + `SHIFT` + `left` = select word to the left (macOS)
    * `CTRL` + `SHIFT` + `right` = select word to the right (Windows)
    * `CTRL` + `SHIFT` + `left` = select word to the left (Windows)
    * `CTRL` + `right` = jump over the word to the right
    * `CTRL` + `left` = jump over the word to the left
    * `CTRL` + `ALT` + L = Reformat Code on Windows
    * `CMD` + `ALT` + L = Reformat Code on macOS

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result_a is not Ellipsis, \
    'Assign your result to variable `result_a`'
    >>> assert result_b is not Ellipsis, \
    'Assign your result to variable `result_b`'
    >>> assert result_c is not Ellipsis, \
    'Assign your result to variable `result_c`'
    >>> assert result_d is not Ellipsis, \
    'Assign your result to variable `result_d`'

    >>> assert type(result_a) is float, \
    'Variable `result_a` has invalid type, should be float'
    >>> assert type(result_b) is float, \
    'Variable `result_b` has invalid type, should be float'
    >>> assert type(result_c) is float, \
    'Variable `result_c` has invalid type, should be float'
    >>> assert type(result_d) is float, \
    'Variable `result_d` has invalid type, should be float'

    >>> result_a
    5.86

    >>> result_b
    3.02

    >>> result_c
    4.14

    >>> result_d
    1.34
"""

DATA = """
sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor
6.3,2.9,5.6,1.8,virginica
6.4,3.2,4.5,1.5,versicolor
"""

# Arithmetic mean of sepal_length column
# type: float
data = (5.8, 5.1, 5.7, 6.3, 6.4)
result_a = sum(data) / len(data)

# Arithmetic mean of sepal_width column
# type: float
data = (2.7, 3.5, 2.8, 2.9, 3.2)
result_b = sum(data) / len(data)

# Arithmetic mean of petal_length column
# type: float
data = (5.1, 1.4, 4.1, 5.6, 4.5)
result_c = sum(data) / len(data)

# Arithmetic mean of petal_width column
# type: float
data = (1.9, 0.2, 1.3, 1.8, 1.5)
result_d = sum(data) / len(data)

