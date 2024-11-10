
result = np.logical_and(DATA < 50, DATA % 2 == 0)
result_all = result.all()
result_any = result.any()
