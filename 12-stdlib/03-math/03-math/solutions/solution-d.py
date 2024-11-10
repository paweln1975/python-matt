
def result(A, B):
    result = []
    A_rows = range(len(A))
    B_rows = range(len(B))
    B_columns = range(len(B[0]))

    for i in A_rows:
        row = []

        for j in B_columns:
            total = 0

            for k in B_rows:
                total += A[i][k] * B[k][j]

            row.append(total)
        result.append(row)

    return result
