#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/asyncio/debug.html

#%% AsyncIO Debug
# By default asyncio runs in production mode
# Asyncio has a debug mode which can be enabled
# More verbose message you can achieve by using PYTHONASYNCIODEBUG=1 and PYTHONTRACEMALLOC=1 environment variables
# Also python3 -X dev -X tracemalloc=5 myfile.py



#%% Debug
# By default asyncio runs in production mode
# Asyncio has a debug mode which can be enabled



#%% Introspection
# asyncio.current_task(loop=None) - Return the currently running Task instance, or None if no task is running.
# asyncio.all_tasks(loop=None) -  Return a set of not yet finished Task objects run by the loop.
# If loop is None, get_running_loop() is used for getting current loop.



#%% Further Reading
# https://docs.python.org/3/library/devmode.html
# https://docs.python.org/3/library/asyncio-dev.html#debug-mode