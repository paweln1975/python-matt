
a = np.random.randint(0, 1025, size=(50, 50))
selection = 2 ** np.arange(11)

mask = np.isin(a, selection)
result = a[mask]
result.sort()
result = np.flip(result)


#%% Alternative Solution
# np.random.seed(0)
#
# MIN = 0
# MAX = 1025
# SIZE = (50, 50)
# SELECT = 2 ** np.arange(11)
#
# a = np.random.randint(MIN, MAX, size=SIZE)
# b = a[np.isin(a, SELECT)]
# result.sort()
# np.flip(result)

#%% Alternative Solution
# sorted(a[np.isin(a, SELECT)], reverse=True)
