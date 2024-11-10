#!/usr/bin/env python3

# Reference:
# https://python3.info/stdlib/modules/import.html

#%% Module Import



#%% Importing modules



#%% Import module
# import ...



#%% Importing function from module
# from ... import ...



#%% Import and alias
# import ... as ...



#%% Relative imports
# from . import ...
# from .. import ...



#%% What is Python Module
# Every Python file is a module
# Every directory with __init__.py file is a module
# Python does not recognize whether it is a file or dir with init
# Useful when you start simple, and then expand
# Usually __init__.py is empty
# If you define __all__: list[str] in __init__.py it will import only those functions when from MODULE import *



#%% Python file is a module



#%% Directory with ``__init__.py`` file



#%% Importing from own modules



#%% Importing variable or constant from module



#%% Importing submodules



#%% Importing all



#%% Importing objects from modules



#%% Importing with aliases



#%% Import path
# Watch-out module names which are the same as in stdlib



#%% ``__name__``
# Zmienna __name__ pozwala ustalić czy dany plik jest wykonywany czy importowany.
# Jeżeli dany plik jest wykonywany, zmienna __name__ ustawiana jest na '__main__'.
# Jeżeli dany plik jest importowany jako moduł, zmienna __name__ ustawiana jest na nazwę modułu.
# Jest to przydatne na przykład przy testowaniu modułów.