#!/usr/bin/env python3
# https://python3.info/advanced/async-asyncio/future.html


# %% AsyncIO Future
# - Low-level awaitable object
# - Represents an eventual result of an asynchronous operation
# - Normally there is *no need* to create Future objects at the application level code
# - When a Future object is awaited it means that the coroutine will wait until the Future is resolved in some other place
# - Future objects in asyncio are needed to allow callback-based code to be used with async/await
# %%



