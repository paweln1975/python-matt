#!/usr/bin/env python3
# https://python3.info/advanced/async-paradigm/coroutine.html


# %% Async Coroutine
# - Coroutine function and coroutine object are two different things
# - Coroutine function is the definition (async def)
# - Coroutine function will create coroutine when called
# - This is similar to generator object and generator function
# - Coroutine functions are not awaitables
# - Coroutine objects are awaitables
# - Coroutines declared with the async/await syntax is the preferred way of writing asyncio applications. [#pydocAsyncioTask]_
# - https://peps.python.org/pep-0492/
# %%



# %% Syntax
# %%



# %% Coroutine Function
# - Coroutine function is the definition (async def)
# - Also known as async functions
# - Defined by putting async in front of the def
# - Only a coroutine function (async def) can use await
# - Non-coroutine functions (def) cannot use await
# - Coroutine functions are not awaitables
# %%



# %% Coroutine Object
# - Coroutine function will create coroutine when called
# - Coroutine objects are awaitables
# - To execute coroutine object you can await it
# - To execute coroutine object you can asyncio.run()
# - To schedule coroutine object: ensure_future() or create_task()
# %%



# %% Run Sequentially
# - All lines inside of coroutine function will be executed sequentially
# %%



# %% Run Concurrently
# - To run coroutine objects use asyncio.gather()
# - This won't execute in parallel (won't use multiple threads)
# - It will run concurrently (in a single thread)
# %%



# %% Error: Created but not awaited
# - Created but not awaited objects will raise an exception
# - This prevents from creating coroutines and forgetting to "await" on it
# %%



# %% Error: Running Coroutine Functions
# - Only coroutine objects can be run
# - It is not possible to run coroutine function
# %%



# %% Error: Multiple Awaiting
# - Coroutine object can only be awaited once
# %%



# %% Error: Await Outside Coroutine Function
# - Only a coroutine function (async def) can use await
# - Non-coroutine functions (def) cannot use await
# %%



# %% Getting Results
# %%



# %% Inspect
# %%



