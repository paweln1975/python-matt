#!/usr/bin/env python3
# https://python3.info/performance/optimization/optimization.html


# %% Optimization Optimization
# - https://wiki.python.org/moin/TimeComplexity
# %%



# %% Contains
# - in checks whether iterable contains value
# - O(n) - in str
# - O(n) - in list
# - O(n) - in tuple
# - O(1) - in set
# - O(1) - in dict
# %%



# %% PyPy
# - http://pypy.org
# - No GIL
# - Can speedup couple order of magnitude
# %%



# %% Patterns
# - Source: [#Shaw2022]_
# %%



# %% Tools
# - memray [#Galindo2022]_
# - tracemalloc
# - mmap - memory allocation
# - Pytest extension for doing benchmarking
# - pip install line_profiler
# %%



# %% Numpy vectorization
# %%



# %% Specialized data structures
# - scipy.spatial - for spatial queries like distances, nearest neighbours, etc.
# - pandas - for SQL-like grouping and aggregation
# - xarray - for grouping across multiple dimensions
# - scipy.sparse - sparse metrics for 2-dimensional structured data
# - sparse (package) - for N-dimensional structured data
# - scipy.sparse.csgraph - for graph-like problems (e.g. finding shortest paths)
# %%



# %% Cython
# - https://numba.pydata.org/
# - https://cython.readthedocs.io/en/latest/
# - https://en.wikipedia.org/wiki/Cython
# - https://youtu.be/zQeYx87mfyw?t=747
# - types
# - Cython files have a .pyx extension
# %%



# %% Numba
# %%



# %% Dask
# - https://dask.org
# %%



# %% Find existing implementation
# - https://pypi.org
# %%



# %% String Concatenation
# %%



# %% String Append
# - Use list.append() instead of str + str:
# %%



# %% Range between two float
# - There are indefinitely many values between two floats
# %%



# %% Deque
# - collections.deque - Double ended Queue
# %%



# %% Further Reading
# - https://wiki.python.org/moin/TimeComplexity
# - https://youtu.be/YY7yJHo0M5I
# - https://visualgo.net/bn/sorting
# - http://sorting.at/
# - https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
# - https://www.youtube.com/watch?v=fOdCxum-qLA
# - https://www.youtube.com/watch?v=zQeYx87mfyw
# - https://www.youtube.com/watch?v=EEUXKG97YRw
# %%



