def two_numbers_sum(iterable, target) -> tuple[int, int] | None:
    """
    Finds two numbers in the iterable that sum up to the target value.
    Args:
        iterable: An iterable object. E.g. list or tuple of integers.
        target: The target sum value.
    Returns:
        Returns their indices as a tuple if found, otherwise returns None.
    Example:
        >>> two_numbers_sum([2, 7, 11, 15], 9)
        (0, 1)
        >>> two_numbers_sum([3, 2, 4], 6)
        (1, 2)
        >>> two_numbers_sum([3, 3], 6)
        (0, 1)
        >>> two_numbers_sum([1, 2, 3], 7) is None
        True
    """
    num_map: dict[int, int] = {}
    for i, num in enumerate(iterable):
        complement = target - num
        if complement in num_map:
            return num_map[complement], i
        num_map[num] = i
    return None