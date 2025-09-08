#!/usr/bin/env python3
# https://python3.info/pandas/series/about.html


# %% Series About
# %%



# %% Info
import pandas as pd

s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s.info(memory_usage='deep')

# - Series.info(memory_usage='deep')
# %%



# %% Non-Null Count  Dtype
# %%



# %% Describe
# - Series.describe()
# %%

s.describe()

date_serie = pd.Series(pd.date_range(start='2025-01-01', end='2025-09-08'))
date_serie.info(memory_usage='deep')
date_serie.describe()

