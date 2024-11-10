
DATA[:, -1].fill(0)
result = DATA.transpose()
result = result.astype(float)
result[0].fill(np.nan)
