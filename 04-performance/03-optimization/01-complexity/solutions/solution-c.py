
features_train = [tuple(X) for *X, y in rows[:split]]
features_test = [tuple(X) for *X, y in rows[split:]]
labels_train = [y for *X, y in rows[:split]]
labels_test = [y for *X, y in rows[split:]]

#%% Alternative Solution
features = [tuple(X) for *X, y in rows]
labels = [y for *X, y in rows]
features_train = features[:split]
features_test = features[split:]
labels_train = labels[:split]
labels_test = labels[split:]

#%% Alternative Solution
train = rows[:split]
test = rows[split:]
features_train = [tuple(X) for *X, y in train]
features_test = [tuple(X) for *X, y in test]
labels_train = [y for *X, y in train]
labels_test = [y for *X, y in test]

# memory complexity - How memory consuming is the task
# computational complexity - How many computations
# cyclomatic complexity - How many loops are in the code, how nested they are
# cognitive complexity - How hard it to understand code (ie. inline bool logic)


"""
# 4.19 µs ± 288 ns per loop (mean ± std. dev. of 100 runs, 10000 loops each)
# 4.01 µs ± 290 ns per loop (mean ± std. dev. of 100 runs, 10000 loops each)
#%%timeit -r 100 -n 10_000
features_train = [tuple(X) for *X,y in data[:split]]
features_test = [tuple(X) for *X,y in data[split:]]
labels_train = [y for *X,y in data[:split]]
labels_test = [y for *X,y in data[split:]]


# 3.86 µs ± 292 ns per loop (mean ± std. dev. of 100 runs, 10000 loops each)
# 3.89 µs ± 278 ns per loop (mean ± std. dev. of 100 runs, 10000 loops each)
#%%timeit -r 100 -n 10_000
features = [tuple(X) for *X,y in data]
labels = [y for *X,y in data]
features_train = features[:split]
features_test = features[split:]
labels_train = labels[:split]
labels_test = labels[split:]


# 3.84 µs ± 297 ns per loop (mean ± std. dev. of 100 runs, 10000 loops each)
# 4 µs ± 268 ns per loop (mean ± std. dev. of 100 runs, 10000 loops each)
#%%timeit -r 100 -n 10_000
train = data[:split]
test = data[split:]
features_train = [tuple(X) for *X,y in train]
features_test = [tuple(X) for *X,y in test]
labels_train = [y for *X,y in train]
labels_test = [y for *X,y in test]



# Python 3.11.1
# Date: 2022-12-23

>>> %%timeit -r 1000 -n 1000
... features_train = [tuple(X) for *X, y in rows[:split]]
... features_test = [tuple(X) for *X, y in rows[split:]]
... labels_train = [y for *X, y in rows[:split]]
... labels_test = [y for *X, y in rows[split:]]
...
...
6.32 µs ± 833 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
>>>
>>>
>>> %%timeit -r 1000 -n 1000
... features = [tuple(X) for *X, y in rows]
... labels = [y for *X, y in rows]
... features_train = features[:split]
... features_test = features[split:]
... labels_train = labels[:split]
... labels_test = labels[split:]
...
...
7.52 µs ± 1.32 µs per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
>>>
>>>
>>> %%timeit -r 1000 -n 1000
... train = rows[:split]
... test = rows[split:]
... features_train = [tuple(X) for *X, y in train]
... features_test = [tuple(X) for *X, y in test]
... labels_train = [y for *X, y in train]
... labels_test = [y for *X, y in test]
...
...
8.48 µs ± 1.49 µs per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)



"""
