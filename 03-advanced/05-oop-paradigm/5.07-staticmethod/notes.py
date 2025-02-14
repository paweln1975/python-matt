#!/usr/bin/env python3
# https://python3.info/advanced/oop-paradigm/staticmethod.html


# %% OOP Staticmethod
# - Method which don't use self in its body should **not** be in a class
# - If method takes self and use it (it requires instances to work) it should be in class
# - If a method don't use self but uses class as a namespace use @staticmethod decorator
# - Using class as namespace
# - No need to create a class instance
# - Will not pass instance (self) as a first method argument
# %%



# %% Problem: Instance Method
# - Instance methods require self as a first argument
# - Calling instance method on a class will result in TypeError
# - Calling instance method on an instance will work
# %%



# %% Problem: Class Function
# - Calling class method on a class will work
# - Calling class method on an instance will result in TypeError
# %%



# %% Solution: Static Method
# - Calling static method on a class will work
# - Calling static method on an instance will work
# - Use @staticmethod decorator to create static method
# %%



# %% Namespace
# %%



# %% When to Use Staticmethod
# - Some functions in a class do not require instance (self) to work
# - Hence, they can be @staticmethod... but should they?
# - @staticmethod is a hint for a developer that method does not use instance
# %%



