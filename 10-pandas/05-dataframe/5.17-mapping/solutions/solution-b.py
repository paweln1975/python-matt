result = (pd
    .read_csv(DATA)
    .replace({'birthdate': MONTHS_PLEN}, regex=True)
    .assign(birthdate=lambda df: pd.to_datetime(df['birthdate']))
    .loc[:, ['firstname', 'lastname', 'birthdate']]
)