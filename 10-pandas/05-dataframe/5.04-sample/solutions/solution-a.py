result = (
    pd
    .read_csv(DATA)
    .sample(frac=1.0)
    .reset_index(drop=True)
    .tail(n=10)
)