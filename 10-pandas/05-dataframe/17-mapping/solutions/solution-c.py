
result = (pd
    .read_csv(DATA, parse_dates=['datetime'], index_col='id')
    .assign(year=lambda df: df['period'].str.split('-', expand=True)[0].astype(int))
    .assign(month=lambda df: df['period'].str.split('-', expand=True)[1].astype(int).map(MONTHS))
)
