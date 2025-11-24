from pair_sum import pair_sum_sorted
def triplets(iterable) -> list[tuple[int, int, int]]:
    """Generate all unique triplets from the given iterable that sum to zero.

    Args:
        iterable: An iterable of elements.
    Yields:
        Tuples of unique triplets.
    Example:
    >>> triplets([2, 4, 6])
    []
    >>> triplets([-1, 0, 1, 2, -1, -4])
    [(-1, -1, 2), (-1, 0, 1)]
    >>> triplets([0, 0, 0, 0])
    [(0, 0, 0)]
    >>> triplets([-2, 0, 1, 1, 2])
    [(-2, 0, 2), (-2, 1, 1)]
    >>> triplets([-3, -2, -1, 0, 1, 2, 3])
    [(-3, 0, 3), (-3, 1, 2), (-2, -1, 3), (-2, 0, 2), (-1, 0, 1)]
    """
    elements = sorted(iterable)
    n = len(elements)
    result: set[tuple[int, int, int]] = set()

    for i in range(n - 2):
        first = elements[i]
        target_sum = -first
        pairs = pair_sum_sorted(elements[i + 1 :], target_sum)
        for left_idx, right_idx in pairs:
            triplet = (first, elements[i + 1 + left_idx], elements[i + 1 + right_idx])
            result.add(triplet)

    return sorted(list(result))