#!/usr/bin/env python3

# Reference:
# https://python3.info/database/sql/sql-join.html

#%% SQL Join
# Combine records from two or more tables in a database
# Combining fields from two tables by using values common to each



#%% INNER JOIN
# Returns rows when there is a match in both tables
# The most important and frequently used of the joins



#%% LEFT JOIN
# Returns all rows from the left table, even if there are no matches in the right table



#%% RIGHT JOIN
# Returns all rows from the right table, even if there are no matches in the left table



#%% FULL JOIN
# Combines the results of both left and right outer joins
# The joined table will contain all records from both the tables and fill in NULLs for missing matches on either side. [#sqljoinfull]_



#%% SELF JOIN
# Is used to join a table to itself as if the table were two tables
# Temporarily renaming at least one table in the SQL statement



#%% CARTESIAN JOIN
# Also known as CROSS JOIN
# Returns the Cartesian product of the sets of records from the two or more joined tables.