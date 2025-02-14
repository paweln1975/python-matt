#!/usr/bin/env python3
# https://python3.info/performance/optimization/profiling.html


# %% Optimization Profiling
# - A profile is a set of statistics that describes how often and for how long various parts of the program executed
# - The profiler modules are designed to provide an execution profile for a given program, not for benchmarking purposes (for that, there is timeit for reasonably accurate results). This particularly applies to benchmarking Python code against C code: the profilers introduce overhead for Python code, but not for C-level functions, and so the C code would seem faster than any Python one.
# %%



# %% Profilers
# - cProfile (CPython built-in)
# - yappi https://github.com/sumerc/yappi
# - PyCharm IDE
# - vmprof https://vmprof.readthedocs.io/en/latest/
# - memory_profiler
# %%



# %% cProfile
# %%



# %% Memory Profiler
# - Memory Profiler is a Python module for monitoring memory consumption of a process as well as line-by-line analysis of memory consumption for Python programs.
# - https://github.com/pythonprofilers/memory_profiler
# - https://pypi.org/project/memory-profiler/
# - pip install memory-profiler
# - python -m memory_profiler myfile.py
# - from memory_profiler import profile, memory_usage
# - @profile
# - usage = memory_usage((func, (arg1, arg2), {'kwarg1': 'val'}))
# - python -m mprof run myfile.py
# - python -m mprof plot
# %%



# %% Yappi
# - Yappi is a high-performance statistical profiler for Python. It is well-suited for profiling multi-threaded applications and handling partial loads of a program.
# - https://github.com/sumerc/yappi
# - https://pypi.org/project/yappi/
# - pip install yappi
# - python -m yappi myfile.py
# - yappi.set_clock_type("cpu") # Use set_clock_type("wall") for wall time
# - yappi.start()
# - yappi.get_func_stats().print_all()
# - yappi.get_thread_stats().print_all()
# %%



