#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/asyncio/3rdparty.html

#%% AsyncIO 3rd Party



#%% Unsync
# Library decides which to run, thread, asyncio or sync



#%% Twisted
# Old project



#%% Gevent
# Actively maintained
# Greenlets (micro-threads running inside one thread)



#%% Tornado
# Actively maintained
# Web framework and asynchronous networking library
# Open-sourced by Facebook after acquisition of FriendFeed



#%% Curio
# Coroutine-based library for concurrent Python systems programming
# Provides standard programming abstractions such as tasks, sockets, files, locks and queues
# Works on POSIX and Windows



#%% Trio
# Python library for async concurrency and I/O
# Focussed on usability and correctness
# Introduced nursery (task groups)



#%% UVLoop
# The ultimate loop implementation for UNIXes (run this on production)