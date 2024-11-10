#!/usr/bin/env python3

# Reference:
# https://python3.info/database/sqlalchemy/connection-engine.html

#%% Connection Engine
# create_engine() builds a factory for database connections
# create_engine() uses Database Source Name (DSN) for configuration
# echo=True - if True, the Engine will log all statements to stdout
# future=True - v2.0 compatibility mode (works only in v1.4)
# Engine is lazily connected
# Engine object supports context managers with block
# engine.connect() method explicitly connects to the database



#%% Glossary



#%% Create Engine



#%% Parameters
# echo=True - if True, the Engine will log all statements to stdout
# future=True - v2.0 compatibility mode (works only in v1.4)
# Full List [#saDocsCreateEngine]_



#%% 2.x Style



#%% Establishing Connection



#%% Show Parameters



#%% Further Reading
# https://docs.sqlalchemy.org/en/stable/core/engines.html#sqlalchemy.create_engine.params.connect_args