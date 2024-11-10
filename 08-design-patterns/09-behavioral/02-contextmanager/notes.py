#!/usr/bin/env python3

# Reference:
# https://python3.info/design-patterns/behavioral/contextmanager.html

#%% Protocol Context Manager
# __enter__(self) -> self
# __exit__(self, *args) -> None
# __leave__() https://github.com/faster-cpython/ideas/issues/550#issuecomment-1410120100
# Since Python 3.10: Parenthesized context managers [#pydocpython310]_
# https://peps.python.org/pep-0707/
# Files
# Buffering data
# Database connection
# Database transactions
# Database cursors
# Locks
# Network sockets
# Network streams
# HTTP sessions
# Since Python 3.10: Parenthesized context managers [#pydocpython310]_
# gh-106 - (exc, val, tb) triplet to one value https://github.com/faster-cpython/ideas/issues/106



#%% Typing
# contextlib.AbstractContextManager
# contextlib.AbstractAsyncContextManager



#%% Contex Manager



#%% Context Decorator Class
# Inherit from contextlib.ContextDecorator
# Class become context manager decorator
# Mind the brackets in decorator @Timeit()



#%% Context Decorator Function
# Split function for parts before and after yield
# Code before yield becomes __enter__()
# Code after yield becomes __exit__()



#%% Many Context Managers
# https://docs.python.org/3/whatsnew/3.10.html#parenthesized-context-managers