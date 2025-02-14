#!/usr/bin/env python3
# https://python3.info/performance/threading/synchronization.html


# %% Threading Synchronization
# - Thread Synchronisation
# %%



# %% Problems
# - Lock Contention - when there is a shared resource which is wanted by many threads very often. Most of the threads will wait for access to that resource
# - Lock Starvation - some threads are more lucky to get more access than the others. There are even some threads which didn't get a lock at all!
# - Deadlock - You cannot access a lock to get a resource, because you haven't acquired a resource in the first place (example: the pharmacy won't sell you mask, because you are not wearing a mask)
# - The more lock, the slower your program is and more memory it uses
# %%



# %% Locks
# - Locks don't lock anything. They are just flags and can be ignored. It is a cooperative tool, not an enforced tool
# - IIn general, locks should be considered a low level primitive that is difficult to reason about nontrivial examples. For more complex applications, you're almost always better of with using atomic message queues.
# - The more locks you acquire at one time, the more you loose the advantages of concurrency
# %%



# %% GIL
# - Global Interpreter Lock
# - CPython has a lock for its internal shared global state
# - One lock instead of hundreds smaller
# - The unfortunate effect of GIL is that no more than one thread can run at a time
# - For I/O bound applications, GIL doesn't present much of an issue
# - For CPU bound applications, using threads makes the application speed worse
# - Accordingly, that drives us to multiprocessing to gain more CPU cycles
# - Larry Hastings, Gilectomy project - removed GIL, but Python slowed down
# %%



# %% Thread Local Storage
# - Operating system mechanism
# - Limits global variables to be seen only by current thread
# - You can keep data around, which are specifically not shared with other threads
# %%



