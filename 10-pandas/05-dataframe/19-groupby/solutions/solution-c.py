
result = (
    pd
    .read_csv(DATA)
    .groupby('name')
    ['name']
    .count()
    .sort_values(ascending=False)
    .head(10)
)
