#!/usr/bin/env python3

# Reference:
# https://python3.info/advanced/asyncio/wait.html

#%% AsyncIO Wait
# asyncio.wait(aws, timeout)
# wait() - when a timeout occurs: does not cancel the futures
# If aw is a coroutine it is automatically scheduled as a Task
# Returns those implicitly created Task objects in (done, pending) sets



#%% Wait
# Coroutine asyncio.wait(aws, *, timeout=None, return_when=ALL_COMPLETED)
# aws must be iterable (list, tuple, set)
# aws iterable must not be empty
# Run awaitable objects in the aws concurrently and block until the condition specified by return_when
# timeout: float|int if specified, maximum number of seconds to wait before returning
# wait() does not cancel the futures when a timeout occurs
# If gather() is cancelled (ie. on timeout), all submitted awaitables (that have not completed yet) are also cancelled
# return_when indicates when this function should return
# return_when must be one of FIRST_COMPLETED, FIRST_EXCEPTION, ALL_COMPLETED
# return_when=FIRST_COMPLETED - The function will return when any future finishes or is cancelled;
# return_when=FIRST_EXCEPTION - The function will return when any future finishes by raising an exception. If no future raises an exception then it is equivalent to ALL_COMPLETED;
# return_when=ALL_COMPLETED - The function will return when all futures finish or are cancelled
# Does not raise asyncio.TimeoutError
# Futures or Tasks that aren't done when the timeout occurs are simply returned in the second set (pending).