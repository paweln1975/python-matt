#!/usr/bin/env python3

# Reference:
# https://python3.info/devops/tests/pytest.html

#%% Pytest
# Detailed info on failing assert statements (no need to remember self.assert* names);
# Auto-discovery of test modules and functions;
# Modular fixtures for managing small or parametrized long-lived test resources;
# Can run unittest (including trial) and nose test suites out of the box;
# Python 3.5+ and PyPy 3;
# Rich plugin architecture, with over 315+ external plugins and thriving community;



#%% Running



#%% Skip



#%% Skipif



#%% ``pytest.raises``



#%% Fixtures
# Fixtures are requested by test functions or other fixtures by declaring them as argument names.
# It's to think of fixtures as a set of resources that need to be set up before a test starts, and cleaned up after.
# @pytest.fixture(scope='module')