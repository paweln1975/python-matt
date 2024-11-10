
def result(A, B):
    if len(A) != len(B):
        raise ValueError('Points must be in the same dimensions')

    under_sqrt = 0

    for n1, n2 in zip(A, B):
        under_sqrt += (n2 - n1) ** 2

    # for index, _ in enumerate(A):
    #     n1 = A[index]
    #     n2 = B[index]
    #     under_sqrt += (n2-n1) ** 2

    # for index in range(len(A)):
    #     n1 = A[index]
    #     n2 = B[index]
    #     under_sqrt += (n2-n1) ** 2

    # number_of_dimensions = len(A)
    # for index in range(number_of_dimensions):
    #     n1 = A[index]
    #     n2 = B[index]
    #     under_sqrt += (n2-n1) ** 2

    return sqrt(under_sqrt)
