result = (
    pd
    .read_csv(DATA)
    .query('Gender == "F"')
    .groupby('Nationality')
    ['Flights']
    .sum()
    .sort_values(ascending=False)
)