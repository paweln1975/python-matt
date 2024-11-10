#!/usr/bin/env python3

# Reference:
# https://python3.info/database/sqlalchemy/about.html

#%% SQLAlchemy About
# ORM converts Python objects to database rows
# ORM converts database rows to Python objects
# ORM provides abstraction over database layer
# ORM allows for object like interaction with database
# ORM provides ability to migrate database schema
# SQAlchemy is the most frequently used database ORM in Python [#PythonDeveloperSurvey2020]_



#%% ORM Pros
# Support for database switching with minimal effort
# Refactoring support (embedded SQL is not easily refactorable)
# 1-to-1 relation of Python class to database table
# Historical migration and change history



#%% ORM Cons
# Some queries could be not well optimized
# Another layer of abstraction
# Another dependency



#%% Database Support
# SQLite3
# PostgreSQL
# Oracle
# MySQL / MariaDB
# MSSQL



#%% Installation



#%% Architecture
# Core
# ORM
# Plugin structure with injection points



#%% 1.x vs 2.x
# future=True flag to create_engine()
# On 2023-01-26 SQLAlchemy 2.0 has been released [#sqlalchemy20]_



#%% Good Practices
# Project Structure
# What is the SQLAlchemy project layout
# Where to store configuration (host, port, schema, username, password)



#%% Alternative ORMs
# Django ORM + Django Migrations [#DjangoORM]_
# SQLModel [#SQLModel]_
# Raw SQL
# SQLObject
# Peewee
# Tortoise ORM
# PonyORM
# Dejavu