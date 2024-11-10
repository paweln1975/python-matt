#!/usr/bin/env python3

# Reference:
# https://python3.info/database/sqlite3/sqlite3-connect.html

#%% SQLite3 Connect
# File database - persistent storage
# In-memory - very fast, but volatile
# sqlite3.connect() -> connection
# connection.close()



#%% In-Memory Database
# Useful for tests, development and demonstrations
# Very fast (do not write any data to disk)
# Remember to close connection



#%% File Database
# Connection will create file if not exists
# Remember to close connection



#%% Context Managers
# Prefer using context manager
# No need to remember about closing connection
# Prepare your data and statements before connection
# Works with either in-memory or file database



#%% Debug
# conn.set_trace_callback(print)
# Registers trace_callback to be called for each SQL statement that is actually executed by the SQLite backend.
# The only argument passed to the callback is the statement (as string) that is being executed.