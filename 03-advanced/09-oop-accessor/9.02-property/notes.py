#!/usr/bin/env python3
# https://python3.info/advanced/oop-accessor/property.html


# %% Accessor Property
# - Disable attribute modification
# - Logging value access
# - Check boundary
# - Raise exceptions such as ValueError or TypeError
# - Check argument type
# %%



# %% Problem
# %%



# %% Solution
# %%



# %% Protocol
# - myattribute = property() - creates property
# - @myattribute.getter - getter for attribute
# - @myattribute.setter - setter for attribute
# - @myattribute.deleter - deleter for attribute
# - Method name must be the same as attribute name
# - myattribute has to be property
# - @property - creates property and a getter
# %%



# %% Property Descriptor
# - name = property() - creates property
# - Preferred way
# %%



# %% Property Decorator
# - @property - creates property and a getter
# - Typically used when, there is only getter and no setter and deleter methods
# %%



# %% Property callable
# - name = property(fget=get_name, fset=set_name, fdel=del_name, doc='docstring for "name" property')
# - Property's arguments are method references get_name, set_name, del_name and a docstring
# - Not recommended
# %%



