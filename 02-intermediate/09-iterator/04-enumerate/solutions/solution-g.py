
def myenumerate(iterable, start=0):
    current = start
    result = []

    for element in iterable:
        row = (current, element)
        result.append(row)
        current += 1

    return result
