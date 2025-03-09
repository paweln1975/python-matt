#!/usr/bin/env python3
# https://python3.info/advanced/oop-inheritance/override.html
import unittest
from json import tool


# %% Inheritance Override
# - Child inherits all fields and methods from parent
# - Used to avoid code duplication
# %%



# %% Override Method
# - Child class will override parent's method
# %%



# %% Override Init
# - __init__() is inherited as any other method
# - Child class will override parent's __init__() method
# - Warning: Call to __init__ of super class is missed
# %%



# %% Override Class Variables
# - Class variables are inherited as any other attribute
# - Child class will override parent's class variable
# %%



# %% Override Instance Variables
# - Instance variables are inherited as any other attribute
# - Child __init__() method will override the parent's __init__() method
# - Child class will override parent's instance variable
# %%


class Robot:
    'Sophisticated robot class'
    def fetch(self, tool):
        print(f'physical fetch {tool=}')
    def move(self, tool):
        print(f'physical move {tool=}')
    def replace(self, tool):
        print(f'physical replace {tool=}')

class CleaningRobot(Robot):
    def clean(self, tool, times=5):
        super().fetch(tool)
        for i in range(times):
            super().move(tool)
        super().replace(tool)

class MockRobot(Robot):
    def __init__(self):
        self.tasks = []

    def fetch(self, tool):
        self.tasks.append(f'fetching {tool=}')

    def move(self, tool):
        self.tasks.append(f'moving {tool=}')

    def replace(self, tool):
        self.tasks.append(f'replacing {tool=}')

class MockedCleaningRobot(CleaningRobot, MockRobot):
    'Inject a mock bot into robot dependency'

class TestCleaningRobot(unittest.TestCase):
    def test_cleaning(self):
        t = MockedCleaningRobot()
        t.clean('mop')

        expected = (["fetching tool='mop'"] +
                    ["moving tool='mop'"] * 5 +
                    ["replacing tool='mop'"])
        self.assertEqual(t.tasks, expected)

if __name__ == '__main__':
    r = CleaningRobot()
    r.clean('broom')
    unittest.main()
