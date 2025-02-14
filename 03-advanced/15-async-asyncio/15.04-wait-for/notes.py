#!/usr/bin/env python3
# https://python3.info/advanced/async-asyncio/wait-for.html


# %% AsyncIO Wait For
# - asyncio.wait_for(aw, timeout: int|float|None)
# - Timeout - number of seconds to wait for
# - If timeout=None, block until the future completes
# - wait_for() - when a timeout occurs: cancels the task and raises asyncio.TimeoutError
# - If aw is a coroutine it is automatically scheduled as a Task
# - If the wait is cancelled, the future aw is also cancelled.
# %%



# %% Wait For
# - The function will wait until the future is actually cancelled
# - Therefore the total wait time may exceed the timeout
# - If an exception happens during cancellation, it is propagated
# - If coroutine does not finish by then, rises TimeoutError
# %%



# %% Handling Timeouts
# %%



# %% Handling Timeouts Concurrently
# %%



# %% Handling Cancellation
# - If gather() is cancelled (ie. on timeout), all submitted awaitables (that have not completed yet) are also cancelled
# %%



# %% Further Reading
# - Langa Ł. How Exception Groups Will Improve Error Handling in AsyncIO [#Langa2022]_
# %%



