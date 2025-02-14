"""
Name: Concurrency Threading Subprocess
Difficulty: easy
Lines: 20
Minutes: 21

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-c.py`

Tests:

Hints:
Ustaw parametr `shell=True` dla `subprocess.run()`

"""

# %% SetUp

import logging
import subprocess
from queue import Queue
from threading import Timer

TIMEOUT = 1.0
DELAY = 1.0
COMMANDS = [
    'ls /home/mwatney',
    'echo "test"',
    'sleep 2',
]

# English
# 1. Create queue `queue` to which you will add various system commands to execute, e.g.:
#    - Linux/macOS: `['ls /tmp/', 'echo "test"', 'sleep 2']`,
#    - Windows: `['dir c:\\Windows', 'echo "test"', 'type %HOMEPATH%\\Desktop\\README.txt']`.
# 2. Then prepare three worker threads that will execute commands from the queue
# 3. Threads should be run as `subprocess.run()` in the operating system with timeout equal to `TIMEOUT = 1.0` second
# 4. The number of commands may increase as the task is performed.
# 5. Threads should be run in the background (`daemon`)
# 6. Run doctests - all must succeed

# Polish
# 1. Stwórz kolejkę `queue` do której dodasz różne polecenia systemowe do wykonania, np.:
#    - Linux/macOS: `['ls /tmp/', 'echo "test"', 'sleep 2']`,
#    - Windows: `['dir c:\\Windows', 'echo "test"', 'type %HOMEPATH%\\Desktop\\README.txt']`.
# 2. Następnie przygotuj trzy wątki workerów, które będą wykonywały polecenia z kolejki
# 3. Wątki powinny być uruchamiane jako `subprocess.run()` w systemie operacyjnym z timeoutem równym `TIMEOUT = 1.0` sekundy
# 4. Ilość poleceń może się zwiększać w miarę wykonywania zadania.
# 5. Wątki mają być uruchomione w tle (ang. `daemon`)
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
