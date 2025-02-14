#!/usr/bin/env python3
# https://python3.info/performance/threading/about.html


# %% Threading About
# - Zaletą wątków jest to, że mają współdzielony stan
# - Jeden wątek może zapisać kod do pamięci a drugi odczytać bez narzutu komunikacyjnego
# - Wadą jest również współdzielony stan i race condition
# - Ideą wątków jest tani dostęp do współdzielonej pamięci, tylko trzeba wszędzie wstawiać locki
# - Run very fast, but hard to get correct
# - It's insanely difficult to create large multi-threaded programs with multiple locks
# - Even if you lock resource, there is no protection if other parts of the system do not even try to acquire the lock
# - Threads switch preemptively
# - Preemptively means that the thread manager decides to switch tasks for you (you don't have to explicitly say to do so). Programmer has to do very little.
# - This is convenient because you don't need to add explicit code to cause a task switch
# - The cost of this convenience is that you have to assume a switch can happen at any time
# - Accordingly, critical sections have to be a guarded with locks
# - The limit on threads is total CPU power minus the cost of tasks switches and synchronization overhead
# - Why Should Async Get All The Love Advanced Control Flow With Threads [#Davis2022]_
# %%



# %% Frequently Asked Questions
# %%



# %% Daemon
# - https://stackoverflow.com/a/190017/228517
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



# %% Thread-safety
# - Thread-safe code is code that will work even if many Threads are executing it simultaneously.
# %%



