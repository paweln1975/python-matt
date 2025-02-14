iris = pd.read_csv(DATA)

ratio = iris["sepal_length"] / iris["sepal_width"]

for name, group in iris.groupby("species"):
    plt.scatter(group.index, ratio[group.index], label=name)

plt.legend()
#plt.show()