#!/usr/bin/env python3
# https://python3.info/advanced/fp-paradigm/closure.html


# %% Functional Pattern Closure
# %%



# %% About
# - Technique by which the data is attached to some code even after end of those other original functions is called as closures
# - When the interpreter detects the dependency of inner nested function on the outer function, it stores or makes sure that the variables in which inner function depends on are available even if the outer function goes away
# - Closures provides some form of data hiding
# - Closures can avoid use of global variables
# - Useful for replacing hard-coded constants
# - Inner functions implicitly carry references to all of the local variables in the surrounding scope that are referenced by the function
# - Since Python 2.2
# %%



# %% Recap
# - Function can access data from outer scope
# - Functions inside their scope can define variables (local scope)
# - Functions inside their scope can define functions (inner functions)
# - Inner functions have access to variables defined in their outer scope (local scope of outer function)
# %%



# %% Return Locals
# %%



# %% What is closure?
# - Closures provides some form of data hiding
# - Closures can avoid use of global variables
# - Useful for replacing hard-coded constants
# %%



# %% How Objects Were Born
# - user - constructor
# - fn - constructor argument (firstname)
# - ln - constructor argument (lastname)
# - firstname - instance variable (field)
# - lastname - instance variable (field)
# - login - instance function (method)
# - logout - instance function (method)
# %%



# %% Decorators
# %%



