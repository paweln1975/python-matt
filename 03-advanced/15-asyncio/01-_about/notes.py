#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/asyncio/_about.html

#%% About
# Latency problem - time from the user action to the appearance of the first UI element user can interact with
# General rule for frontend frameworks - don't block the foreground, let the long running operations to run in background, and leave the user interface interactive
# Concurrency and Parallelism



#%% Classification of concurrency problems
# Martelli Model of Scalability
# 1 core: Single thread and single process
# 2-8 cores: Multiple threads and multiple processes
# 9+ cores: Distributed processing



#%% GIL
# Global Interpreter Lock
# CPython has a lock for its internal shared global state
# One lock instead of hundreds smaller
# The unfortunate effect of GIL is that no more than one thread can run at a time
# For I/O bound applications, GIL doesn't present much of an issue
# For CPU bound applications, using threads makes the application speed worse
# Accordingly, that drives us to multiprocessing to gain more CPU cycles
# Larry Hastings, Gilectomy project - removed GIL, but Python slowed down



#%% Process



#%% Thread



#%% Async
# Running asynchronously: 3s + 1s + 1s = bit over 3s [execution time]
# Async is the future of programming



#%% Sync vs Async



#%% Threads vs Processes



#%% Threads vs Async
# Threads are about workers and async is about tasks
# Async maximizes CPU utilization because it has less overhead than threads.
# Threading typically works with existing code and tools as long as locks are added around critical sections
# For complex systems, async is much easier to get right than threads with locks
# Threads require very little tooling (locks and queues)
# Async needs a great deal of tooling (futures, event loops, and non-blocking version of just about everything.



#%% Context Switching
# Threads, thread manager does it automatically for you
# In Async, you specify places to context switch
# Time consuming
# Za każdym razem kiedy robisz print() kod automatycznie wykonuje Context Switch



#%% Testing
# In concurrent programs (threading, multiprocessing) testing can hide bugs and errors
# Some lines of code works so fast, that it requires million runs to make errors to appear
# But if you put sleep() than errors will show up
# In Internet of Things (IoT) I'd prefer to stand in front of a car which has code written in async way, than a threaded way
# Async is profoundly easier to debug and get it right



#%% Rules