#!/usr/bin/env python3
# https://python3.info/design-patterns/decorator/about-mechanics.html


# %% Decorator Mechanics
# %%



# %% Recap
# - When you define a function, Python will do several things
# - Python will create a function object
# - Python will compile function body to bytecode and assign it to the funcobj.__code__.co_code
# - Python will add function name (identifier) to the globals() (name will be a reference of the function object)
# - When you call a function, Python will call funcobj.__call__() method which will execute it's bytecode (funcobj.__code__.co_code)
# %%



# %% Function Definition
# %%



# %% Create an Alias
# %%



# %% Helper Function
# - debug content was executed at the moment of decorating the function (not calling it)
# %%



# %% Delay Execution
# - We need to delay the execution of the debug function content
# %%



# %% Make New Behavior Permanent
# - If we define alias with the same name as the original function
# - globals()['hello'] will point not to hello() but to debug() function
# - This will make the new behavior permanent
# %%



# %% Decorator Syntax
# - @debug is just a shortcut to hello = debug(hello)
# %%



