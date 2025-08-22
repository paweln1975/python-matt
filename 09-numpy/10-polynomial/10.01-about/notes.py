#!/usr/bin/env python3
# https://python3.info/numpy/polynomial/about.html
import numpy as np

# %% Polynomial About
# %%



# %% Defining
# %%



# %% Find Coefficients
# - Find the coefficients of a polynomial with the given sequence of roots
# - Specifying the roots of a polynomial still leaves one degree of freedom,
# %%



# %% Roots
# - Return the roots of a polynomial
# %%

p1 = np.poly1d([2, -1])
roots1 = np.roots(p1)
print(roots1)

p2 = np.poly1d([1, 0, -1])
roots2 = np.roots(p2)
print(roots2)

values = np.polyval(p2, roots2)
print(values)

# create numpy array from -100 to 100 with step 1
x_vals = np.arange(-100, 101, 1)
y_vals = np.polyval(p2, x_vals)
print(y_vals)


# %% Derivative of a Polynomial
# %%



# %% Antiderivative (indefinite integral) of a polynomial
# - Return an antiderivative (indefinite integral) of a polynomial
# %%



# %% Evaluate a Polynomial at Specific Values
# - Compute polynomial values
# - Horner's scheme is used to evaluate the polynomial
# %%



# %% Least Squares Polynomial Fit
# - Least squares polynomial fit
# %%



# %% Polynomial Arithmetic
# - np.polyadd()
# - np.polysub()
# - np.polymul()
# - np.polydiv()
# %%



# %% Sum of Two Polynomials
# %%



