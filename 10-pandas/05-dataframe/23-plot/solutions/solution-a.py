
result = (
    pd.read_excel(
        io=DATA,
        parse_dates=['datetime'],
        sheet_name='Luminance',
        header=1,
        index_col=0)
    .query('location == @WHERE')
    .loc[WHEN, 'value']
    .apply(np.sign)
    .resample('h')
    .sum())

plot = (result
     .plot(color='red', figsize=(10,10), yticks=[0,1])
     .set_yticklabels(['seep', 'awake'])
)
