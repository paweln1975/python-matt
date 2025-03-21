def print_multipliers(n: int, count: int = 10):
    """"
    Given an integer n print its first  multiples. Each multiple n x i should be printed on a new line
    in the form: n x i = result.
    For count = 3 the output will be:
    3 x 1 = 3
    3 x 2 = 6
    3 x 3 = 9
    >>> print_multipliers(3, 10)
    3 x 1 = 3
    3 x 2 = 6
    3 x 3 = 9
    3 x 4 = 12
    3 x 5 = 15
    3 x 6 = 18
    3 x 7 = 21
    3 x 8 = 24
    3 x 9 = 27
    3 x 10 = 30
    """
    for i in range(1, count + 1):
        result = n * i
        print(f"{n} x {i} = {result}")
