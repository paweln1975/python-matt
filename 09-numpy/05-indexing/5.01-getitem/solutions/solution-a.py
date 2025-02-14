result = np.empty(shape=(2,2), dtype=float)
result[0,0] = DATA[0,2]
result[0,1] = DATA[2,2]
result[1,0] = DATA[0,0]
result[1,1] = DATA[1,0]

# %% Alternatively
# result = np.array([
#     DATA[0][2],
#     DATA[2][2],
#     DATA[0][0],
#     DATA[1][2],
# ], float).reshape(2, 2)

# %% Alternatively
# result = np.array([
#     [DATA[0,2], DATA[2,2]],
#     [DATA[0,0], DATA[1,0]],
# ], float)