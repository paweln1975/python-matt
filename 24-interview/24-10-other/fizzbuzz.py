def fizz_buzz(n: int) -> list[str]:
    """Generate a list of strings representing the FizzBuzz sequence up to n.
    Args:
        n (int): The upper limit of the sequence (inclusive).
    Returns:
        list[str]: A list of strings representing the FizzBuzz sequence.
        Elements divisible by 3 are replaced with "Fizz", elements divisible by 5 with "Buzz",
        and elements divisible by both 3 and 5 with "FizzBuzz".
    Example:
        >>> fizz_buzz(15)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        >>> fizz_buzz(5)
        ['1', '2', 'Fizz', '4', 'Buzz']
        >>> fizz_buzz(1)
        ['1']
        >>> fizz_buzz(0)
        []
        >>> fizz_buzz(3)
        ['1', '2', 'Fizz']
        >>> fizz_buzz(10)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']
        >>> fizz_buzz(20)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz']
    """
    result = ['FizzBuzz' if i % 3 == 0 and i % 5 == 0
                        else 'Fizz' if i % 3 == 0
                        else 'Buzz' if i % 5 == 0
                        else str(i) for i in range(1, n + 1)]
    return result
