#!/usr/bin/env python3
# https://python3.info/database/sqlalchemy/connection-pool.html


# %% SQLAlchemy Connection Pool
# - Establishing a new database connection is time consuming
# - Connection Pool - a collection of connections, which lives longer than requests
# - Establish several connections at the beginning
# - Add them to the so called 'connection pool'
# - Use them for request processing
# - After request is process the connection is returned to the pool
# %%



# %% Usage
# %%



# %% Parameters
# - echo_pool=False
# - max_overflow=10
# - pool=None
# - poolclass=None
# - pool_logging_name
# - pool_pre_ping=True
# - pool_recycle=-1
# - pool_reset_on_return='rollback'
# - pool_size=5
# - pool_timeout=30
# - pool_use_lifo=False
# %%



# %% Pool Implementations
# %%



# %% Keep Alive
# %%



# %% Further Reading
# - http://docs.sqlalchemy.org/en/latest/core/pooling.html
# %%



