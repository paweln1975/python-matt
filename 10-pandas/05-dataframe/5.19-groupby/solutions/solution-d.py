result = (
    pd
    .read_csv(DATA, sep=';')
    .assign(EV1=lambda df: df['Participants'].str.split(',', expand=True)[0].str.strip())
    .assign(EV2=lambda df: df['Participants'].str.split(',', expand=True)[1].str.strip())
    .assign(EV3=lambda df: df['Participants'].str.split(',', expand=True)[2].str.strip())
    .astype({'Duration': 'timedelta64[s]'})
    .convert_dtypes()
    .melt(id_vars=['Duration'], value_vars=['EV1', 'EV2', 'EV3'], value_name='Astronaut')
    .dropna()
    .set_index('Astronaut')
    .loc[:, ['Duration']]
    .groupby('Astronaut')
    .sum()
    .sort_values(by='Duration', ascending=False)
    .head(10)
)