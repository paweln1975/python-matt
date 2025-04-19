def is_prime(number):
    """
    Checks if a given number is a prime number.

    Args:
        number: The number to check for primality.

    Returns:
        True if the number is prime, False otherwise.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is less than 2.
    """
    # Input validation:
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")

    if number <= 1:
        return False
    # 2 is a special case, it's the only even prime number
    if number == 2:
        return True

    # Optimization: Check only odd numbers up to the square root of the number
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False

    return True


data_count = int(input())
result = []
for i in range(data_count):
    result.append(is_prime(int(input())))

for r in result:
    print('Prime' if r == 1 else 'Not prime')