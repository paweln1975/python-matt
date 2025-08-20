import numpy as np
DATA = 'iris.csv'

header = np.loadtxt(DATA, max_rows=1, dtype='str', delimiter=',', usecols=(0,1,2,3))
values = np.loadtxt(DATA, skiprows=1, dtype='float', delimiter=',', usecols=(0,1,2,3))
species = np.loadtxt(DATA, skiprows=1, dtype='str', delimiter=',', usecols=4)


sepal_length = (header == 'sepal_length')
sepal_width = (header == 'sepal_width')
petal_length = (header == 'petal_length')
petal_width = (header == 'petal_width')

setosa = (species == 'setosa')
versicolor = (species == 'versicolor')
virginica = (species == 'virginica')

print(values[setosa, sepal_length])
print(values[setosa, sepal_width].mean().round(2))
