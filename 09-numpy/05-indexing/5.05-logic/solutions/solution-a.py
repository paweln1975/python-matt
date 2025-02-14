data = np.logical_and(DATA < 50, DATA % 2 == 0)
result_a = data.all()
result_b = data.any()