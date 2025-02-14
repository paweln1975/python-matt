#!/usr/bin/env python3
# https://python3.info/database/sqlalchemy/orm-about.html


# %% SQLAlchemy ORM About
# - ORM - Object Relational Mapping
# - Process of associating object oriented classes with database tables
# - Set of object oriented classes is a domain model (business model)
# - The most basic task is to translate between domain object and a table row
# - Any tool which takes database row and converts this to an object is an ORM
# - ORM represents basic compositions: one-to-many, many-to-one using foreign key
# - ORM allows to querying the database in terms of the domain model structure
# - Some ORM can represent class inheritance hierarchies using variety of schemes
# - Some ORMs can handle 'sharding' of data, i.e. storing a domain model across multiple schemas or databases
# - Provide various patterns for concurrency, including row versioning
# - Provide patterns for data validation and coercion
# %%



# %% Flavors
# - Active Record or Data Mapper
# - Declarative or Imperative style configuration
# %%



# %% Active Record
# - Active Record has domain objects handle their own persistence
# - Every object is a row in a table
# - Notion of objects working in a transaction is a secondary notion
# %%



# %% Data Mapper
# - Tries to keep the details of persistence separate from the object being persisted
# - It is more explicit
# - Does not use globals and threaded locals
# - Always create connection, transaction and explicitly say when to commit
# %%



# %% Declarative Style Configuration
# - Classes and attributes
# - Attributes names columns in a database
# %%



# %% Imperative Style Configuration
# - There was a plan to remove Imperative Style from SQLAlchemy 2.0, but stayed
# - The class is not completely agnostic, because mapper heavily influence design
# %%



# %% SQLAlchemy ORM
# - SQLAlchemy ORM is essentially a data mapper style ORM
# - Most users use declarative configuration style
# - Imperative style and a range of variants in between are supported as well
# - Extends SQLAlchemy Core, in particular extending the SQL Expression language
# - Designed to work with domain classes as well as table constructs
# - Key features: Unit of Work, Identity Map, Lazy / Eager loading
# - Unit of Work - accumulates INSERT/UPDATE/DELETE statements and transparently sends it to the database in batch
# - Identity Map - objects are kept unique in memory based on their primary key identity
# - Lazy / Eager loading - related attributes and collections can be loaded either on-demand (lazy) or upfront (eager)
# - Source: [#ytSQLAlchemy20]_
# %%



# %% ORM
# - SQLAlchemy mappings in 1.4/2.0 start with a central object known as 'registry'
# - Has a collection of metadata inside it
# - Traditional Declarative Base uses Python metaclass
# - This gets in a way, when you want to uses metaclass on your own
# - In such case you can use mapper registry decorator
# %%



# %% Object Statuses
# - Transient - object created, but not yet added to the session
# - Pending - object added to a session but not yet stored in database
# - Persistent - represent an active row in a database (object is stored)
# - Detached
# - Pending Delete
# %%



# %% Adding Objects
# %%



# %% Making Changes
# - Add more objects to be pending for flush
# - .add_all() is the same as .add(), but adds a list of objects
# %%



# %% Rolling Back Changes
# %%



# %% ORM Querying
# %%



# %% Relationships, Joins
# %%



# %% Querying with Multiple Tables
# %%



# %% Eager Loading
# %%



