#!/usr/bin/env python3
# https://python3.info/stdlib/modules/distributing.html


# %% Module Distributing
# %%



# %% Installing Packages
# - pip search
# - pip install
# - pip install -r requirements.txt
# %%



# %% __init__.py
# - Since Python 3.3 - :pep:420 -- Implicit Namespace Packages
# - https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/__init__.py
# - https://github.com/django/django/blob/master/django/views/generic/__init__.py
# %%



# %% __all__
# - https://github.com/django/django/blob/master/django/views/generic/__init__.py
# %%



# %% Creating packages
# %%



# %% TOML
# - PEP 518 -- Specifying Minimum Build System Requirements for Python Projects
# - https://www.python.org/dev/peps/pep-0518/
# - https://snarky.ca/what-the-heck-is-pyproject-toml/
# %%



# %% distutils
# - Provides support for building and installing additional modules into a Python.
# - The new modules may be either 100%-pure Python, or may be extension modules written in C, or may be collections of Python packages which include modules coded in both Python and C.
# %%



# %% setuptools
# - Enhanced alternative to distutils that provides:
# %%



# %% wheel vs. egg
# - to build a python wheel package
# - sdist will generate a .tar.gz file in dist/
# - bdist_wheel will generate a .whl file in dist/
# %%



# %% requirements.txt vs. setup.py
# %%



# %% setup.py
# %%



# %% setup.cfg
# - Configuring setup() using setup.cfg files
# - A setup.py file containing a setup() function call is still required even if your configuration resides in setup.cfg.
# %%



# %% python setup.py sdist upload
# - upload is deprecated in favor of using twine
# %%



# %% twine
# %%



# %% Signing packages
# %%



# %% Artifactory
# - https://www.jfrog.com/confluence/display/RTF/PyPI+Repositories#PyPIRepositories-PublishingtoArtifactory
# %%



# %% Further Reading
# - https://www.youtube.com/watch?v=jOiAp3wtx18
# - https://www.youtube.com/watch?v=Oc9khbXBes8
# %%



