import unittest
"""
Given a base-10 integer, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum
number of consecutive 1's in n's binary representation. When working with different bases, it is common to show
the base as a subscript.
"""

def convert_to_binary(n: int) -> str:
    """
    Convert an integer to its binary representation without the '0b' prefix.

    Args:
        n: A base-10 integer

    Returns:
        Binary representation as a string

    >>> convert_to_binary(23)
    '10111'
    """
    return str(bin(n))[2:]

def check_bin(s: str) -> bool:
    return s in ['1', '0']

def max_consecutive_values_in_binary(n: int, value: str = '1'):
    """
    Find the maximum number of consecutive 1's (as default) in the binary representation of n.

    Args:
        n: A base-10 integer

    Returns:
        Maximum count of consecutive 1's

    >>> max_consecutive_values_in_binary(23)
    3

    >>> max_consecutive_values_in_binary(0)
    0

    >>> max_consecutive_values_in_binary(255)
    8

    >>> max_consecutive_values_in_binary(1)
    1

    >>> max_consecutive_values_in_binary(15)
    4
    """
    max_length = 0
    binary = convert_to_binary(n)
    if not all(map(check_bin, binary)):
        raise ValueError('Wrong values in bin representation.')

    max_current = 0
    for v in binary:
        if v == value:
            max_current += 1
            max_length = max(max_current, max_length)
        else:
            max_current = 0

    return max_length


def max_consecutive_ones_in_binary_bitwise(n: int) -> int:
    """
    Find the maximum number of consecutive 1's using bitwise operations.
    >>> max_consecutive_ones_in_binary_bitwise(23)
    3

    >>> max_consecutive_ones_in_binary_bitwise(0)
    0

    >>> max_consecutive_ones_in_binary_bitwise(255)
    8

    >>> max_consecutive_ones_in_binary_bitwise(1)
    1

    >>> max_consecutive_ones_in_binary_bitwise(15)
    4
    """
    max_count = 0
    current_count = 0

    while n > 0:
        if n & 1:  # Check if least significant bit is 1
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
        n >>= 1  # Right shift by 1

    return max_count


class TestMaxConsecutiveOnes(unittest.TestCase):

    def test_zero(self):
        """Test case for n = 0 (binary: 0)"""
        self.assertEqual(max_consecutive_ones_in_binary_bitwise(0), 0)

    def test_one(self):
        """Test case for n = 1 (binary: 1)"""
        self.assertEqual(max_consecutive_ones_in_binary_bitwise(1), 1)

    def test_power_of_two(self):
        """Test case for n = 4 (binary: 100)"""
        self.assertEqual(max_consecutive_ones_in_binary_bitwise(4), 1)

    def test_consecutive_ones(self):
        """Test case for n = 7 (binary: 111)"""
        self.assertEqual(max_consecutive_ones_in_binary_bitwise(7), 3)

    def test_alternating_bits(self):
        """Test case for n = 10 (binary: 1010)"""
        self.assertEqual(max_consecutive_ones_in_binary_bitwise(10), 1)

    def test_multiple_sequences(self):
        """Test case for n = 23 (binary: 10111)"""
        self.assertEqual(max_consecutive_ones_in_binary_bitwise(23), 3)

    def test_large_number(self):
        """Test case for n = 255 (binary: 11111111)"""
        self.assertEqual(max_consecutive_ones_in_binary_bitwise(255), 8)

    def test_separated_ones(self):
        """Test case for n = 273 (binary: 100010001)"""
        self.assertEqual(max_consecutive_ones_in_binary_bitwise(273), 1)

    def test_trailing_zeros(self):
        """Test case for n = 24 (binary: 11000)"""
        self.assertEqual(max_consecutive_ones_in_binary_bitwise(24), 2)

    def test_leading_ones(self):
        """Test case for n = 15 (binary: 1111)"""
        self.assertEqual(max_consecutive_ones_in_binary_bitwise(15), 4)

    def test_very_large_number(self):
        """Test case for a very large number with known consecutive ones"""
        # 2^20 - 1 = 1048575 (binary: 11111111111111111111)
        self.assertEqual(max_consecutive_ones_in_binary_bitwise(1048575), 20)

    def test_complex_pattern(self):
        """Test case for n = 1775 (binary: 11011101111)"""
        self.assertEqual(max_consecutive_ones_in_binary_bitwise(1775), 4)


if __name__ == '__main__':
    unittest.main()
