#!/usr/bin/env python3

# Reference:
# https://python3.info/pandas/series/statistics.html

#%% Series Statistics



#%% Count
# Series.count() - Number of non-null observations
# Series.nunique() - Number of unique values
# Series.value_counts() - Frequency of unique values
# Series.size - Number of elements
# len(Series) - Number of elements



#%% Sum
# Series.sum() - Sum of values
# Series.cumsum() - Cumulative sum



#%% Product
# Series.prod() - Product of values
# Series.cumprod() - Cumulative product



#%% Extremes
# Series.min() - Minimum value
# Series.idxmin() - Index of minimum value (Float, Int, Object, Datetime, Index)
# Series.argmin() - Range index of minimum value
# Series.cummin() - Cumulative minimum
# Series.max() - Maximum value
# Series.idxmax()  - Index of maximum value (Float, Int, Object, Datetime, Index)
# Series.argmax()  - Range index of maximum value
# Series.cummax()  - Cumulative maximum



#%% Average
# Series.mean() - Arithmetic mean of values
# Series.median() - Median of values
# Series.mode() - Mode of values
# Series.rolling(window=2).mean() - Rolling average



#%% Distribution
# Series.abs() - Absolute value
# Series.std() - Standard deviation
# Series.sem() - Standard Error of the Mean (SEM)
# Series.skew() - Skewness (3rd moment)
# Series.kurt() - Kurtosis (4th moment)
# Series.quantile() - Sample quantile (value at %)
# Series.var() - Variance
# Series.corr() - Correlation Coefficient



#%% Describe
# Series.describe() - Summary statistics