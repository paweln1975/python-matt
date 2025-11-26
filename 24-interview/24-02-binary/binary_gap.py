def binary_gap(n: int) -> int:
    """Find the longest sequence of consecutive zeros that is surrounded by ones
    at both ends in the binary representation of a positive integer n.

    Args:
        n (int): A positive integer.
    Returns:
        int: The length of the longest binary gap.
        If there is no binary gap, return 0 e.g. for n = 15 (binary 1111).
    Example:
        >>> binary_gap(9)  # binary: 1001
        2
        >>> binary_gap(529)  # binary: 1000010001
        4
        >>> binary_gap(20)  # binary: 10100
        1
        >>> binary_gap(15)  # binary: 1111
        0
        >>> binary_gap(32)  # binary: 100000
        0
        >>> binary_gap(1041)  # binary: 10000010001
        5
        >>> binary_gap(1)  # binary: 1
        0
        >>> binary_gap(88439847398)  # binary: 1010010010111011011001111100111100110
        2

    """
    binary_repr = bin(n)[2:]  # Get binary representation without '0b' prefix
    binary_repr_rev = reversed(list(map(int, binary_repr)))
    max_len = 0
    current_len = 0
    in_gap = False
    for b in binary_repr_rev:
        if b:
            if in_gap:
                max_len = max(max_len, current_len)
                current_len = 0
            in_gap = True
        else:
            if in_gap:
                current_len += 1
    return max_len
