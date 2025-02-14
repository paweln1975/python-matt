result = (
    pd
    .read_csv(DATA)
    .groupby('name')
    ['name']
    .count()
    .sort_values(ascending=False)
    .head(9)
    .reset_index(name='flights')
    .sort_values(by=['flights','name'], ascending=[False, True])
)