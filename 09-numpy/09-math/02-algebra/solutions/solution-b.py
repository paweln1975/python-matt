
def result(a, b):
    if len(a) != len(b):
        raise ValueError('Points must be in the same dimensions')

    under_sqrt = 0

    for n1, n2 in zip(a, b):
        under_sqrt += (n2-n1) ** 2

    return sqrt(under_sqrt)
