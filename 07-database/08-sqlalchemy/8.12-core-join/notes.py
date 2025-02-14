#!/usr/bin/env python3
# https://python3.info/database/sqlalchemy/core-join.html


# %% SQLAlchemy Core Join
# %%



# %% Select Multiple Tables
# - SELECT from more than one table
# - This will render CARTESIAN JOIN
# - This can crash systems if tables are big
# - Since SQLAlchemy 1.4 library will warn on cartesian products
# %%



# %% Join From
# - New in SQLAlchemy 1.4
# - Have some additional features than join()
# - More explicitly
# - Is better to start chain of joins
# %%



# %% Join
# - join() will infer the left hand side automatically
# - Is better for continuing chain of joins
# %%



# %% Join On
# - You can specify the column on which to perform a join
# - Useful when there is several ForeignKey columns
# - If SQLAlchemy cannot find join column automatically it throws an error
# %%



# %% Table Aliases
# - Python will use object identity to distinguish objects
# %%



# %% Subqueries
# %%



# %% Subqueries Group By
# - SQLAlchemy uses column correspondence
# - It uses column names to identify implicit foreign keys
# - Example: astronaut_id will be joined with astronaut.id
# %%



# %% Common Table Expressions
# - CTE - Common Table Expressions
# - Very popular PostgreSQL feature
# - Could be used with SELECT, UPDATE and DELETE
# - Like a Subquery, but not in the FROM clause
# - It resides above query and uses syntax WITH
# - Allow recursive queries
# - Can produce very optimized forms
# - Postgres can optimize CTE better than subqueries
# - In SQLAlchemy it is used exactly the same way as subqueries
# %%



# %% Correlated Subqueries
# - A subquery in the columns clause or in the WHERE clause of the enclosing SELECT statement
# - Should return exactly one row and one column
# - Used as a column expression in bigger column query
# %%



