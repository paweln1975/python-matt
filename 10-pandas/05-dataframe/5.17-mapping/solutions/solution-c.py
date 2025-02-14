result = (pd
    .read_csv(DATA)
    .assign(
        year=lambda df: df['period'].str.split('-', expand=True)[0],
        month=lambda df: df['period'].str.split('-', expand=True)[1])
    .astype({'month': int})
    .replace({'month': MONTHS})
)