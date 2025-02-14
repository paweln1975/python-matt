data = np.arange(0, 20, 2)
result = pd.Series(data)

# %% Alternatively
# result = pd.Series(range(0, 20, 2))

# %% Alternatively
# result = pd.Series([x for x in range(0, 20) if x % 2 == 0])