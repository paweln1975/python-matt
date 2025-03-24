def print_array_in_reversed_order(input_list: list[int]):
    """
    Given an array of integers, print elements in reverse order as a single line of space-separated numbers
    >>> print_array_in_reversed_order([1, 2, 3, 4])
    4 3 2 1

    >>> print_array_in_reversed_order(list(range(20)))
    19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

    """

    reversed_list = input_list[::-1]
    print(*reversed_list)



if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().rsplit().split()))
    print_array_in_reversed_order(numbers)
