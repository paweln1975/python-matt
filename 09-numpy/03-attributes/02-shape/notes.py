#!/usr/bin/env python3

# Reference:
# https://python3.info/numpy/attributes/shape.html

#%% Array Shape
# Any shape operation changes only np.ndarray.shape and np.ndarray.strides and does not touch data



#%% Recap



#%% Shape



#%% Reshape
# Returns new array
# Does not modify inplace
# a.reshape(1, 2) is equivalent to a.reshape((1, 2))



#%% Flatten
# Returns new array (makes memory copy - expensive)
# Does not modify inplace



#%% Ravel
# Ravel is the same as Flatten but returns a reference (or view) of the array if possible (i.e. memory is contiguous)
# Otherwise returns new array (makes memory copy)



#%% Flatten vs Ravel



#%% Recap