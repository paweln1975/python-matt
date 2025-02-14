def result(A, B):
    if len(A) != len(B):
        raise ValueError('Points must be in the same dimensions')

    under_sqrt = sum((n2-n1)**2 for n1,n2 in zip(A,B))
    return sqrt(under_sqrt)