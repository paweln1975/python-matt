"""
Hacker rank Day-11 challenge task
"""
def convert_input_into_data(data: str) -> list[list[int]]:
    """
    Converts string data into two-dimensional table
    :param data:
    :return:
    """
    arr = []
    for line in data.rstrip().splitlines():
        arr.append(list(map(int, line.rstrip().split())))
    return arr

def calculate_max_hourglass_sum(arr: list[list[int]]) -> int:
    """
    Calculates the maximum sum of hourglasses in the 2D array.

    An hourglass is defined as:
       a b c
         d
       e f g

    Args:
        arr: A 2D array of integers

    Returns:
        The maximum hourglass sum
    """
    max_sum = -5 * 5
    for x in range(1, len(arr)-1):
        for y in range(1, len(arr)-1):
            hour_glass_sum = (arr[y-1][x-1] + arr[y-1][x]
                              + arr[y-1][x+1] + arr[y][x]
                              + arr[y+1][x-1] + arr[y+1][x] + arr[y+1][x+1])

            max_sum = max(max_sum, hour_glass_sum)

    return max_sum


if __name__ == '__main__':

    DATA = """1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 2 4 4 0
    0 0 0 2 0 0
    0 0 1 2 4 0
    """

    input_data = convert_input_into_data(DATA)
    value = calculate_max_hourglass_sum(input_data)
    print(value)

