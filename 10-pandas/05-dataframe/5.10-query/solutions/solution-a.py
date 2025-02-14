result = (
    pd
    .read_csv(DATA)
    .query('petal_length > 2.0')
    .head(n=5)
)