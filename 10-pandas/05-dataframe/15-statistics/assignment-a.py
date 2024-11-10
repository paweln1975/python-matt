"""
* Assignment: DataFrame Statistics
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    1. Modify `df: pd.DataFrame` (cars dataset)
    2. Add column `status` with values:
        a. `old` if `mileage` above 100_000 km
        b. `young` if `mileage` from 10_000 km to 100_000 km
        c. `new` if `mileage` from 0 to 10_000 km
    3. Using `pd.cut` add column `type`:
        a. if `consumption` is 0 or 1 `type` is `electric`
        b. if `consumption` from 2 to 10 (inclusive) `type` is `car`
        c. if `consumption` is 11 or more, `type` is `truck`
    4. Analyze data statistically:
        a. Save basic descriptive statistics (`DataFrame.describe()`) to `result: pd.DataFrame`
        b. Check group count (`DataFrame.count()`, `Series.value_counts()`)
    5. Run doctests - all must succeed

Polish:
    1. Zmodyfikuj `df: pd.DataFrame`` (zestaw danych o samochodach)
    2. Dodaj kolumnę `status` o wartościach:
        a. `old` jeżeli `mileage` powyżej 100_000 km
        b. `young` jeżeli `mileage` od 10_000 km do 100_000 km
        c. `new` jeżeli `mileage` od 0 do 10_000 km
    3. Używając `pd.cut` dodaj kolumnę `type`:
        a. jeżeli `consumption` to 0 lub 1 `type` to `electric`
        b. jeżeli `consumption` od 2 do 10 (włącznie) `type` to `car`
        c. jeżeli `consumption` to 11 lub więcej, `type` to `truck`
    4. Przeanalizuj dane statystycznie:
        a. Zapisz podstawowe statystyki opisowe (`DataFrame.describe()`) do `result: pd.DataFrame`
        b. Sprawdź liczność grup (`DataFrame.count()`, `Series.value_counts()`)
    5. Uruchom doctesty - wszystkie muszą się powieść

Extra:
    1. (wymaga wiedzy z przyszłych rozdziałów)
    2. Narysuj histogram dla `consumption`
    3. Pogrupuj dane po `type` i `status` a następnie wypisz statystyki opisowe
    4. Pogrupuj dane po `type` i `status`, wypisz statystyki opisowe a następnie je transponuj

Run:
    * PyCharm: right-click in the editor and pick `Run Doctest in myfile`
    * PyCharm: `Control + Shift + R`
    * Terminal: `python -m doctest -v myfile.py`
    * In order to show plot in PyCharm or Python script, use `plt.show()` command
    * But first import it from `from matplotlib import pyplot as plt`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 10)
    >>> pd.set_option('display.max_rows', 10)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is pd.DataFrame, \
    'Variable `result` must be a `pd.DataFrame` type'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
                mileage  consumption
    count      50.00000    50.000000
    mean   110421.02000     9.320000
    std     53170.24328     6.244802
    min      7877.00000     0.000000
    25%     71239.75000     4.000000
    50%    115186.00000     9.000000
    75%    154889.00000    14.750000
    max    199827.00000    20.000000
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

np.random.seed(0)


df = pd.DataFrame({
    'mileage': np.random.randint(0, 200_000, size=50),
    'consumption': np.random.randint(0, 21, size=50),
})


# type: pd.DataFrame
result = ...


