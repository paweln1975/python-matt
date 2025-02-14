#!/usr/bin/env python3
# https://python3.info/advanced/fp-paradigm/scope.html


# %% Functional Scope
# - Values defined in function does not leak out
# - Functions has access to global values
# - Shadowing is when you define variable with name identical to the one from outer scope
# - Shadowing in a function is valid only in a function
# - After function return, the original value of a shadowed variable is restored
# - global keyword allows modification of global variable
# - Using global keyword is considered as a bad practice
# %%



# %% Local Scope
# - Values defined in function does not leak out
# %%



# %% Locals
# %%



# %% Global Scope
# - Functions has access to global values
# %%



# %% Globals
# - In the globals scope: globals() has all the objects from the global scope
# - In the global scope: globals() is the same as locals()
# - In the function scope: globals() is the same as in global scope
# - In the function scope: locals() has only variables from inside of a function
# %%



# %% Shadowing
# - When variable in function has the same name as in outer scope
# - Shadowing in a function is valid only in a function
# - Shadowed variable will be deleted upon function return
# - After function return, the original value of a shadowed variable is restored
# %%



# %% Modify Global
# %%



# %% Global Keyword
# - global keyword allows modification of global variable
# - Using global keyword is considered as a bad practice
# %%



# %% NonLocal Scope
# %%



# %% Nonlocal
# - Python nonlocal keyword is used to reference a variable in the nearest scope
# %%



