"""The AdvancedArithmetic interface and the method declaration for the abstract divisorSum(n) method are
 provided for you in the editor below.

Complete the implementation of Calculator class, which implements the AdvancedArithmetic interface.
The implementation for the divisorSum(n) method must return the sum of all divisors of n.

Example
The divisors of 20 are 1, 2, 4, 5, 10, 20 and their sum is 42.
"""

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    """
    >>> c = Calculator()
    >>> c.divisorSum(20)
    42
    """
    def divisorSum(self, n):
        divisors = [i for i in range(1, n + 1) if n % i == 0]
        return sum(divisors)


n = int(42)
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)