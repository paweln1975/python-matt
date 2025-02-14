def result(A, B):
    x1 = A[0]
    y1 = A[1]
    x2 = B[0]
    y2 = B[1]

    dx = (x2-x1)
    dy = (y2-y1)

    return sqrt(dx**2 + dy**2)