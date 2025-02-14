result = (
    pd
    .read_csv(DATA, names=COLUMNS, skiprows=1)
    .replace({'species': {0:'setosa', 1:'versicolor', 2:'virginica'}})
    .where(lambda df: df['petal_length']>=4.0, pd.NA)
    .dropna(how='any', axis='rows')
    .head(n=2)
)