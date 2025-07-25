import unittest

def split_and_join(line):
    """
    Splits the input string by spaces and joins with hyphens.

    Args:
        line (str): A string of space-separated words.

    Returns:
        str: The resulting string joined by hyphens.
    """
    return '-'.join(line.split())

def swap_case(s):
    """
    Swaps the case of each letter in the input string.

    Args:
        s (str): The string to modify.

    Returns:
        str: The modified string with swapped cases.
    """
    return s.swapcase()


# write unit tests for the split_and_join function
class TestSplitAndJoin(unittest.TestCase):
    def test_split_and_join(self):
        self.assertEqual(split_and_join("this is a string"), "this-is-a-string")
        self.assertEqual(split_and_join("hello world"), "hello-world")
        self.assertEqual(split_and_join("split and join"), "split-and-join")
        self.assertEqual(split_and_join(""), "")
        self.assertEqual(split_and_join("singleword"), "singleword")

# write unit tests for the swap_case function
class TestSwapCase(unittest.TestCase):
    def test_swap_case(self):
        self.assertEqual(swap_case("Hello World"), "hELLO wORLD")
        self.assertEqual(swap_case("Python"), "pYTHON")
        self.assertEqual(swap_case("12345"), "12345")  # Numbers should remain unchanged
        self.assertEqual(swap_case(""), "")  # Empty string should remain empty
        self.assertEqual(swap_case("aBcDeF"), "AbCdEf")  # Mixed case