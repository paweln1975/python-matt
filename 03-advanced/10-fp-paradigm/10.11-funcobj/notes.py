#!/usr/bin/env python3
# https://python3.info/advanced/fp-paradigm/funcobj.html


# %% Functional Function Object
# %%



# %% Name
# - function.__name__
# - function.__qualname__
# %%



# %% Type
# - type(function)
# - function.__class__
# - function.__class__.__name__
# - function.__class__.__qualname__
# - function.__class__.__text_signature__
# %%



# %% Annotations
# %%

def parameter_printer(func):
    argnames = func.__code__.co_varnames
    def wrapper(*args, **kwargs):
        arguments = dict(zip(argnames, args)) | kwargs
        for argname, argvalue in arguments.items():
            print(f'{argname}={argvalue}')
        return func(*args, **kwargs)
    return wrapper

@parameter_printer
def add(a, b):
    print(a+b)

add(1, 2)
add(a=3, b=5)

# %% Signature
# %%



# %% Doc
# - help(function)
# - function.__doc__
# %%



# %% Call
# - callable(function)
# - function()
# - function.__call__()
# %%



# %% Function Code
# - add.__code__
# - add.__code__.co_code
# %%



# %% Function Location
# - add.__code__.co_filename
# - add.__code__.co_firstlineno
# %%



# %% Function Arguments
# - add.__code__.co_varnames
# - add.__code__.co_kwonlyargcount
# - add.__code__.co_posonlyargcount
# - add.__code__.co_argcount
# %%



# %% Setattr, Getattr
# %%



