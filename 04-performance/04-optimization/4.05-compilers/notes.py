#!/usr/bin/env python3
# https://python3.info/performance/optimization/compilers.html


# %% Optimization Compilers and Interpreters
# - https://docs.python.org/3/library/py_compile.html
# - https://docs.python.org/3/library/compileall.html#module-compileall
# - https://docs.python.org/3/library/zipapp.html
# %%



# %% cPython
# %%



# %% Cython
# - https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html
# %%



# %% PyPy
# %%



# %% IronPython
# %%



# %% Jython
# %%



# %% Micropython
# - MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments.
# - MicroPython is packed full of advanced features such as an interactive prompt, arbitrary precision integers, closures, list comprehension, generators, exception handling and more. Yet it is compact enough to fit and run within just 256k of code space and 16k of RAM.
# - MicroPython aims to be as compatible with normal Python as possible to allow you to transfer code with ease from the desktop to a microcontroller or embedded system.
# - In addition to implementing a selection of core Python libraries, MicroPython includes modules such as "machine" for accessing low-level hardware.
# - https://micropython.org/
# - IoT
# %%



# %% Pyston
# - Pyston is an open-source faster implementation of the Python programming language, designed for the performance and compatibility challenges of large real-world applications.
# - Pyston was started at Dropbox in 2014 in order to reduce the costs of its rapidly-growing Python server fleet.
# - In 2019 the Pyston developers regrouped without a corporate sponsor and started investigating alternative approaches to speeding up Python. They ended up deciding to fork CPython 3.8, and by early 2020 they restarted the project in a new codebase, and called it "Pyston v2". The first version of Pyston v2 was released in late 2020.
# - In mid-2021 the Pyston developers joined Anaconda, which since then has provided funding for the project and packaging expertise.
# - https://www.pyston.org/
# - https://github.com/pyston/pyston
# %%



# %% GPython
# - gpython is a part re-implementation, part port of the Python 3.4 interpreter in Go.
# - https://github.com/go-python/gpython
# %%



# %% RustPython
# - RustPython is a Python interpreter written in Rust.
# - RustPython can be embedded into Rust programs to use Python as a scripting language for your application, or it can be compiled to WebAssembly in order to run Python in the browser.
# - RustPython is free and open-source under the MIT license.
# - https://rustpython.github.io/
# %%



# %% Cinder
# - Cinder is Meta's (Facebook/Instagram) internal performance-oriented production version of CPython 3.8.
# - It contains a number of performance optimizations, including bytecode inline caching, eager evaluation of coroutines, a method-at-a-time JIT, and an experimental bytecode compiler that uses type annotations to emit type-specialized bytecode that performs better in the JIT.
# - Cinder is powering Instagram, where it started, and is increasingly used across more and more Python applications in Meta.
# - https://github.com/facebookincubator/cinder
# %%



# %% PyScript
# - framework that allows users to create rich Python applications in the browser using a mix of Python with standard HTML. PyScript aims to give users a first-class programming language that has consistent styling rules, is more expressive, and is easier to learn.
# - https://pyscript.net/
# - https://github.com/pyscript/pyscript
# - https://anaconda.cloud/pyscript-pycon2022-peter-wang-keynote
# %%



# %% HPy
# - HPy provides a new API for extending Python in C.
# - In other words, you use #include <hpy.h> instead of #include <Python.h>.
# - Zero overhead on CPython: extensions written in HPy runs at the same speed as "normal" extensions.
# - Much faster on alternative implementations such as PyPy, GraalPython.
# - Debug Mode: in debug mode, you can easily identify common problems such as memory leaks, invalid lifetime of objects, invalid usage of APIs. Have you ever forgot a Py_INCREF or Py_DECREF? The HPy debug mode will detect these mistakes for you.
# - Universal binaries: extensions built for the HPy Universal ABI can be loaded unmodified on CPython, PyPy, GraalPython, etc.
# - Nicer API: the standard Python/C API shows its age. HPy is designed to overcome some of its limitations, be more consistent, produce better quality extensions and to make it harder to introduce bugs.
# - Evolvability: As nicely summarized in [PEP-620](https://peps.python.org/pep-0620/) the standard Python/C API exposes a lot of internal implementation details which makes it hard to evolve the C API. HPy doesn't have this problem because all internal implementation details are hidden.
# - https://hpyproject.org/
# %%



# %% GraalPython
# - High-Performance. Modern Python
# - On average, Python in GraalVM is 8.92x faster than CPython and 8.34x faster than Jython
# - GraalVM provides a Python 3.8 compliant runtime.
# - A primary goal of the GraalVM Python runtime is to support SciPy and its constituent libraries, as well as to work with other data science and machine learning libraries from the rich Python ecosystem.
# - https://www.graalvm.org/python/
# %%



# %% Mypyc
# - Mypyc compiles Python modules to C extensions.
# - It uses standard Python type hints to generate fast code.
# - https://mypyc.readthedocs.io/en/latest/
# %%



# %% Nuitka
# - https://www.nuitka.net
# %%



# %% Others
# %%



# %% Compiling
# - https://py2app.readthedocs.io/
# - http://www.py2exe.org/
# - http://www.pyinstaller.org/
# %%



