#!/usr/bin/env python3
# https://python3.info/numpy/operations/broadcasting.html


# %% Operations Broadcasting
# %%



# %% Broadcasting Rules
# - Source [#NumpyBroadcastingRules]_
# %%



# %% Addition
# %%



# %% Subtraction
# %%



# %% True Division
# %%



# %% Floor Division
# %%



# %% Modulo
# %%



# %% Power
# %%



# %% Root
# %%



# %% Array Multiplication
# - Multiplication * remains elementwise
# - Does not correspond to matrix multiplication
# %%



# %% Matrix Multiplication
# %%



# %% Dot
# - np.dot()
# - If either a or b is 0-D (scalar), it is equivalent to multiply and using numpy.multiply(a, b) or a * b is preferred.
# - If both a and b are 1-D arrays, it is inner product of vectors (without complex conjugation).
# - If both a and b are 2-D arrays, it is matrix multiplication, but using matmul or a @ b is preferred.
# - If a is an N-D array and b is a 1-D array, it is a sum product over the last axis of a and b.
# - If a is an N-D array and b is an M-D array (where M>=2), it is a sum product over the last axis of a and the second-to-last axis of b: dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])
# %%



