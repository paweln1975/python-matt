#!/usr/bin/env python3
# https://python3.info/numpy/about/numpy.html


# %% About Numpy
# - NumPy is the fundamental package for scientific computing with Python
# - a powerful N-dimensional array object
# - sophisticated (broadcasting) functions
# - tools for integrating C/C++ and Fortran code
# - useful linear algebra, Fourier transform, and random number capabilities
# %%



# %% Installation
# %%



# %% Further Reading
# - http://www.labri.fr/perso/nrougier/teaching/numpy.100/
# - https://github.com/rougier/numpy-100
# %%

import numpy as np

# Define your system
A = np.array([
    [13.8, 5.8, 2.4, 1],
    [42.9, 12.3, 3.5, 1],
    [85.2, 19.4, 4.4, 1],
    [125.0, 25.0, 5.0, 1]
])

b = np.array([0.0111, 0.0142, 0.02, 0.025])

# Solve the system
try:
    solution = np.linalg.solve(A, b)

    variables = ['b', 'c', 'd', 'e']
    print("Solution:")
    for i, var in enumerate(variables):
        print(f"{var} = {solution[i]:.12f}")

    # Verify solution
    verification = np.allclose(np.dot(A, solution), b)
    print(f"\nVerification (should be True): {verification}")

except np.linalg.LinAlgError:
    print("The system has no unique solution. It might be singular or inconsistent.")

