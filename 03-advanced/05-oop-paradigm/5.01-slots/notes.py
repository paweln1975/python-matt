#!/usr/bin/env python3
# https://python3.info/advanced/oop-paradigm/slots.html


# %% OOP Slots
# - Slots are faster and save memory
# - Slots prevent from adding new attributes
# - Slotted classes don't have __dict__ and __weakref__
# - Slotted classes have __slots__ and slotted attributes
# - Slots do not affect methods or __init__()
# - Slots do not inherit, unless subclass is also slotted
# %%



# %% Definition
# - Add __slots__ to class definition
# - It could be list[str] or tuple[str] or dict[str,str]
# - Format of dict[str,str] is used for docstrings of slotted fields
# %%



# %% Under the Hood
# - Unslotted classes will have __dict__ and __weakref__
# - Slots will not have __dict__ and __weakref__
# - Slots will have __slots__ and slotted attributes
# %%



# %% Setattr
# - In unslotted classes you can add attributes dynamically
# - Slots disables adding attributes dynamically
# %%



# %% Getattr
# - You can access slotted attributes as normal
# %%



# %% Methods
# - Slots do not affect methods
# - You can define methods as usual
# - You can access slotted attributes inside methods
# %%



# %% Init
# - Slots do not affect __init__()
# - You can define it as usual
# - You can set slotted attributes inside __init__()
# - You cannot assign to not slotted attribute
# %%



# %% Vars and __dict__
# - Slots will prevent from creating __dict__
# - Builtin function vars() will not work on slots
# - vars() requires __dict__
# %%



# %% Recreating Vars Behavior
# - To get values iterate over self.__slots__ and use getattr(self, x)
# - {x:getattr(mark,x) for x in mark.__slots__}
# %%



# %% Fallback
# - User.__slots__ = ('firstname', 'lastname', '__dict__')
# %%



# %% Inheritance Problem
# - Slots do not inherit, unless they are specified in subclass
# - Slots are added on inheritance
# - If class does not specify slots, the __dict__ will be added
# %%



# %% Inheritance Solution
# %%



# %% Dataclasses
# - Since Python 3.10
# - Parameter @dataclass(slots=True) will add slots to the class
# %%



# %% Recap
# - Slots are faster and save memory
# - Slots prevent from adding new attributes
# - Slotted classes don't have __dict__ and __weakref__
# - Slotted classes have __slots__ and slotted attributes
# - Slots do not affect methods or __init__()
# - Slots do not inherit, unless subclass is also slotted
# %%



# %% Further Reading
# - https://docs.python.org/3/reference/datamodel.html#slots
# - https://stackoverflow.com/questions/472000/usage-of-slots
# %%



