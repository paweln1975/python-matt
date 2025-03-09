#!/usr/bin/env python3
# https://python3.info/advanced/oop-inheritance/mixin.html


# %% Inheritance Mixins
# %%
from dataclasses import dataclass

@dataclass
class Diamond0:
    def __init__(self):
        print("Diamond0 init")

    def print_mro(self):
        print(self.__class__.__mro__)

@dataclass
class Diamond1(Diamond0):
    param1: int = 0
    param2: int = 1

    def print_params(self):
        print(self.param1, self.param2)

@dataclass
class Diamond2(Diamond0):
    param1: int = 0
    param2: int = 1

    def print_params(self):
        print(self.param2, self.param1)


@dataclass()
class DiamondProblem(Diamond1, Diamond2):
    def __init__(self):
        super().__init__()
        print("DiamondProblem init")


diamond = DiamondProblem()
print(diamond.param1, diamond.param2)
diamond.print_params()
diamond.print_mro()
