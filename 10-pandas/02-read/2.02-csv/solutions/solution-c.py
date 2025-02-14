header = pd.read_csv(DATA, nrows=0)
nrows, nvalues, *labels = header.columns
decoder = dict(enumerate(labels))

result = (
    pd
    .read_csv(DATA, names=COLUMNS, skiprows=1)
    .replace(to_replace={'label': decoder})
    .head(n=25)
)