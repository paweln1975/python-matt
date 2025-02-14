#!/usr/bin/env python3
# https://python3.info/design-patterns/creational/builder.html


# %% Builder
# - EN: Builder
# - PL: Budowniczy
# - Type: object
# - Why: To separate the construction of an object from its representation
# - Why: The same construction algorithm can be applied to different representations
# - Usecase: Export data to different formats
# %%



# %% Pattern
# %%



# %% Problem
# - Violates Open/Close Principle
# - Tight coupling between Presentation class with formats
# - PDF has pages, Movies has frames, this knowledge belongs to somewhere else
# - Duplicated code
# - Magic number
# %%



# %% Solution
# - Use the builder pattern to separate the exporting logic from the presentation format
# - The same exporting logic belongs to the different formats
# %%



