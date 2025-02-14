#!/usr/bin/env python3
# https://python3.info/advanced/async-asyncio/run.html


# %% AsyncIO Run
# - asyncio.run() is a main entrypoint
# - asyncio.gather() can run concurrently and gather result (in order of its arguments)
# %%



# %% Run Coroutine
# - asyncio.run(coro, *, debug=False)
# - Execute the coroutine coro and return the result
# - Takes care of managing the asyncio event loop, finalizing asynchronous generators, and closing the threadpool
# - Cannot be called when another asyncio event loop is running in the same thread
# - Always creates a new event loop and closes it at the end
# - It should be used as a main entry point for asyncio programs, and should ideally only be called once
# %%



# %% Run Sequentially
# %%



# %% Run Concurrently
# - awaitable asyncio.gather(*aws, return_exceptions=False)
# - Run awaitable objects in the aws sequence concurrently
# - If any awaitable in aws is a coroutine, it is automatically scheduled as a Task
# - If all awaitables are completed successfully, the result is an aggregate list of returned values
# - The order of result values corresponds to the order of awaitables in aws
# - return_exceptions=False (default): the first raised exception is immediately propagated to the task that awaits on gather(); other awaitables in the aws sequence won't be cancelled and will continue to run
# - return_exceptions=True: exceptions are treated the same as successful results, and aggregated in the result list
# - If gather() is cancelled (ie. on timeout), all submitted awaitables (that have not completed yet) are also cancelled
# - If any Task or Future from the aws sequence is cancelled, it is treated as if it raised CancelledError – the gather() call is not cancelled in this case
# - This is to prevent the cancellation of one submitted Task/Future to cause other Tasks/Futures to be cancelled
# %%



# %% Run as Completed
# - asyncio.as_completed(aws, *, timeout=None)
# - Run awaitable objects in the aws iterable concurrently
# - Return an iterator of coroutines
# - Each coroutine returned can be awaited to get the earliest next result from the iterable of the remaining awaitables
# - Raises asyncio.TimeoutError if the timeout occurs before all Futures are done
# %%



# %% Run in Threads
# - coroutine asyncio.to_thread(func, /, *args, **kwargs)
# - Asynchronously run function func in a separate thread.
# - Any *args and **kwargs supplied for this function are directly passed to func.
# - Return a coroutine that can be awaited to get the eventual result of func.
# - This coroutine function is intended to be used for executing IO-bound functions/methods that would otherwise block the event loop if they were ran in the main thread.
# %%



