#!/usr/bin/env python3
# https://python3.info/advanced/async-paradigm/event-loop.html


# %% Async Event Loop
# - Async code can only run inside an event loop.
# - The event loop is the driver code that manages the cooperative multitasking.
# - You can create multiple threads and run different event loops in each of them.
# - Python will create a default event loop only in Main Thread
# - Python will not create an event loop automatically for you on any other than main thread by default, this is to prevent from having multiple event lops created explicitly
# - Event loop can execute only one callback (coroutine) at a time
# - Some callbacks (coroutines) can schedule themselves once again (trampoline)
# - Reactors
# - Proactors
# %%



# %% Selectors
# %%



# %% Loop
# %%



# %% UVLoop
# - The ultimate loop implementation for UNIXes (run this on production)
# %%



