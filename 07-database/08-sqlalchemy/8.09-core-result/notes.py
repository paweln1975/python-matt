#!/usr/bin/env python3
# https://python3.info/database/sqlalchemy/core-result.html


# %% SQLAlchemy Core Result
# - .all()
# - .first()
# - .one() - returns exactly one row
# - .one_or_none()
# %%



# %% List[tuple]
# - It will download all the data from database
# - This technique is not particularly efficient for large databases
# %%



# %% List[dict]
# - It will download all the data from database
# - This technique is not particularly efficient for large databases
# %%



# %% One
# - Must be exactly one result, otherwise the exception is raised
# - Exception MultipleResultsFound
# %%



# %% One or None
# %%



# %% All
# %%



# %% First
# - Fetches the first result from a cursor object
# - CursorResult object has no attribute 'last'
# %%



# %% Columns
# %%



# %% Scalars
# - When you have a row, but there is only one column that you care about
# - We don't want the rows back, we want a list of values
# %%



