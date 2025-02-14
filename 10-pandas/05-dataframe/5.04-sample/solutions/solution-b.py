result = (
    pd
    .read_csv(DATA)
    .ffill()
    .sample(frac=1)
    .reset_index(drop=True)
    .astype({'Order': 'int'})
)