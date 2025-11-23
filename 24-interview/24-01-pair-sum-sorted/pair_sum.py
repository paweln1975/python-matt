def pair_sum_sorted(iterable, target_sum) -> list[tuple]:
    """Finds all unique pairs in a sorted iterable that sum to target_sum.

    Args:
        iterable: A sorted iterable of numbers (e.g., list, tuple).
        target_sum: The target sum for the pairs.
    Returns:
        A list of unique index pairs (tuples) that sum to target_sum.
    Example:
        >>> pair_sum_sorted([1, 2, 3, 4, 5], 5)
        [(0, 3), (1, 2)]
        >>> pair_sum_sorted([-2, 0, 1, 3, 4, 5], 3)
        [(0, 5), (1, 3)]
        >>> pair_sum_sorted([1, 1, 2, 2, 3, 4], 4)
        [(0, 4), (1, 4), (2, 3)]
        >>> pair_sum_sorted([], 5)
        []
        >>> pair_sum_sorted([1], 1)
        []
        >>> pair_sum_sorted([2, 3], 5)
        [(0, 1)]
        >>> pair_sum_sorted([2, 4], 5)
        []
        >>> pair_sum_sorted([2, 2, 3], 5)
        [(0, 2), (1, 2)]
        >>> pair_sum_sorted([-1, 2, 3], 2)
        [(0, 2)]
        >>> pair_sum_sorted([-3, -2, -1], -5)
        [(0, 1)]
    """
    left = 0
    right = len(iterable) - 1
    result = []

    while left < right:
        current_sum = iterable[left] + iterable[right]
        if current_sum == target_sum:
            result.append((left, right))
            # look at the next one from left, if the same, move left pointer
            if left < right and iterable[left + 1] == iterable[left]:
                left += 1
            elif right > left and iterable[right - 1] == iterable[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1

    return result