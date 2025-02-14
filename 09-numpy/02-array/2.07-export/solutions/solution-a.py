species = np.loadtxt(DATA, delimiter=',', dtype='str', max_rows=1, usecols=(2, 3, 4))
features = np.loadtxt(DATA, delimiter=',', dtype='float', skiprows=1, usecols=(0, 1, 2, 3))
labels = np.loadtxt(DATA, delimiter=',', dtype='int', skiprows=1, usecols=4)