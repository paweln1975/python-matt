def print_even_odd_chars(s: str):
    """
    Given a string of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed
    characters as 2 space-separated strings on a single line
    >>> print_even_odd_chars('adbecf')
    abc def

    >>> print_even_odd_chars('LoremIpsumLoremIpsumLoremIpsumLoremIpsumLoremIpsum')
    LrmpuLrmpuLrmpuLrmpuLrmpu oeIsmoeIsmoeIsmoeIsmoeIsm
    """

    even_chars = s[0::2]
    odd_chars = s[1::2]
    print(even_chars, odd_chars)


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        value = input()
        print_even_odd_chars(value)
