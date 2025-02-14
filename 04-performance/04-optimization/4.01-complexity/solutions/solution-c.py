features_train = [tuple(X) for *X, y in rows[:split]]
features_test = [tuple(X) for *X, y in rows[split:]]
labels_train = [y for *X, y in rows[:split]]
labels_test = [y for *X, y in rows[split:]]

# %% Alternatively
features = [tuple(X) for *X, y in rows]
labels = [y for *X, y in rows]
features_train = features[:split]
features_test = features[split:]
labels_train = labels[:split]
labels_test = labels[split:]

# %% Alternatively
train = rows[:split]
test = rows[split:]
features_train = [tuple(X) for *X, y in train]
features_test = [tuple(X) for *X, y in test]
labels_train = [y for *X, y in train]
labels_test = [y for *X, y in test]