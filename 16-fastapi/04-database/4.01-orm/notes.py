#!/usr/bin/env python3
# https://python3.info/fastapi/database/orm.html


# %% Database ORM
# - ORM - Object-relational mapping
# - ORM has tools to convert (map) between objects in code and database tables (relations)
# - Declarative - First define model, which then maps to the database tables
# - If you want to generate
# %%



# %% Install
# %%



# %% Connection
# %%



# %% Models
# - Represents database entity
# %%



# %% Schema
# - Represents JSON request/response data
# - Config.from_attributes = True is required to have model as a response_model (a decorator parameter).
# - Note, that if you set from_attributes = True, then not all fields need to be specified.
# - Listed fields will be in response, and not listed will be hidden in response.
# %%



# %% Further Reading
# - https://fastapi.tiangolo.com/tutorial/sql-databases/
# - https://www.sqlalchemy.org
# %%



