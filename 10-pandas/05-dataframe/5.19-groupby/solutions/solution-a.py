result = (
    pd
    .read_csv(DATA, parse_dates=['datetime'])
    .assign(year=lambda df: df['datetime'].dt.year)
    .assign(month=lambda df: df['datetime'].dt.month)
    .query('item == "call"')
    .groupby(['year', 'month'])['duration']
    .sum()
)