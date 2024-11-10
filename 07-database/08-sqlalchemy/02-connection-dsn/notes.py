#!/usr/bin/env python3

# Reference:
# https://python3.info/database/sqlalchemy/connection-dsn.html

#%% Connection DSN
# DSN - Database Source Name
# Format: db://user:password@host:port/database?opt1=val1&opt2=val2
# :rfc:1738 -- Uniform Resource Locators (URL) [#RFC1738]_



#%% Data Source Name
# the name of the data source
# the location of the data source
# the name of a database driver which can access the data source
# a user ID for data access (if required)
# a user password for data access (if required)



#%% SQLite3
# https://docs.sqlalchemy.org/en/stable/dialects/sqlite.html
# Supported versions 3.12+
# In-memory mode
# File mode



#%% PostgreSQL
# https://docs.sqlalchemy.org/en/stable/dialects/postgresql.html
# Supported versions 9.6+



#%% MySQL and MariaDB
# https://docs.sqlalchemy.org/en/stable/dialects/mysql.html
# MariaDB is an open-source fork of MySQL (after it was bought by Oracle)
# SQLAlchemy supports MySQL and all modern versions of MariaDB
# Minimum MySQL version supported is now 5.0.2



#%% Oracle
# https://docs.sqlalchemy.org/en/stable/dialects/oracle.html
# Supported versions 11+



#%% MSSQL
# https://docs.sqlalchemy.org/en/stable/dialects/mssql.html
# Supported versions 2012+
# pymssql is currently not included in SQLAlchemy's continuous integration (CI) testing.



#%% URL Create



#%% Good Practice
# Split configuration parameter from its call
# Place configuration in separate file which can be imported