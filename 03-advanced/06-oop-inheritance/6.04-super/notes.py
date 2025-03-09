#!/usr/bin/env python3
# https://python3.info/advanced/oop-inheritance/super.html


# %% Inheritance Super
# - Raymond Hettinger - Super considered super! - PyCon 2015 [#Hettinger2015]_
# %%



# %% Problem
# %%



# %% Solution
# %%



# %% Super Order
# - Order is important
# %%



# %% Super Init
# - Call to __init__ of super class is missed
# %%



# %% Init and Multiple Inheritance
# %%


class Eve(object): pass
class Adam(object): pass
class Ramon(Adam, Eve): pass
class Gayle(Adam, Eve): pass
class Raymond(Ramon, Gayle): pass
class Denis(Adam, Eve): pass
class Sharon(Adam, Eve): pass
class Rachel(Denis, Sharon): pass
class Matthew(Raymond, Rachel): pass

help(Matthew)
