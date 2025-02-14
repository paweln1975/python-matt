#!/usr/bin/env python3
# https://python3.info/django/orm/lookup.html


# %% ORM Lookup
# %%



# %% Empty
# - __isnull
# %%



# %% Sequences
# - __in - value in a list
# %%



# %% Strings
# - __exact - value exactly matches text (case sensitive) - this is default behavior if no lookup is provided
# - __iexact - value exactly matches text (case insensitive)
# - __contains - value contains text (case sensitive)
# - __icontains - value contains text (case insensitive)
# - __endswith - value ends with text (case sensitive)
# - __iendswith - value ends with text (case insensitive)
# - __startswith - value starts with text (case sensitive)
# - __istartswith - value starts with text (case insensitive)
# %%



# %% Numeric, Dates
# - __eq - value equal to
# - __gt - value greater than
# - __gte - value greater or equal than
# - __lt - value less than
# - __lte - value less or equal than
# - __range - value between lower and upper bounds (upper bound included)
# %%



# %% Dates
# - __year - year part of a datetime or date value
# - __month - month part of a datetime or date value
# - __day - day part of a datetime or date value
# - __hour - hour part of a datetime or time value
# - __minute - minute part of a datetime or time value
# - __second - second part of a datetime or time value
# - __microsecond - microsecond part of a datetime or time value
# %%



# %% Relationships
# %%



# %% The pk Lookup
# %%



