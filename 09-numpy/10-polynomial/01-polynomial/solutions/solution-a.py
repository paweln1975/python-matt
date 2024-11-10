
data = np.array(DATA[1:])
x = data[:, 0]
y = data[:, 1]

result = np.polyfit(x, y, deg=3)
