#!/usr/bin/env python3
# https://python3.info/numpy/statistics/reduction.html

import numpy as np

# %% Statistics Reduction
# %%



# %% Sum
# - a.sum()
# - np.sum()
# - np.nansum()
# %%



# %% Cumulative Sum
# - a.cumsum()
# - np.cumsum()
# - np.nancumsum()
# %%



# %% Product
# - a.prod()
# - np.prod()
# - np.nanprod()
# %%



# %% Cumulative Product
# - a.cumprod()
# - np.cumprod()
# - np.nancumprod()
# %%



# %% Mean
# - a.mean()
# - np.mean()
# - np.nanmean()
# %%



# %% Cumulative Mean
# - a.cummean()
# - np.cummean()
# - np.nancummean()
# %%



# %% Variance
# - a.var()
# - np.var()
# - np.nanvar()
# %%

arr1 = np.array([[0, 0, 14, 14], [0, 6, 8, 14], [6, 6, 8, 8]])
print("arr1 variance:", arr1.var(axis=1))
print("arr1 stddev:", arr1.std(axis=1))

arr1 = arr1[0]
var1 = ((arr1 - arr1.mean()) ** 2).mean()
print("var1:", var1)
std1 = var1 ** 0.5
print("std1:", std1)


# %% Standard Deviation
# - a.std()
# - np.std()
# - np.nanstd()
# %%



# %% Minimal Value
# - np.ndarray.argmin() index of an np.ndarray.min() element in array
# - np.nanmin()
# - np.nanargmin()
# %%



# %% Maximal Value
# - np.ndarray.argmax() index of an a.max() element in array
# - np.nanmax()
# - np.nanargmax()
# %%



# %% Median
# - np.median()
# - np.nanmedian()
# %%



# %% Quantile
# - np.quantile()
# - np.nanquantile()
# %%



# %% Percentile
# - np.percentile()
# - np.nanpercentile()
# %%



