
result = (
    pd
    .read_xml(StringIO(DATA))
    .loc[:, 'price']
    .str.removesuffix(' USD')
    .astype('float64')
    .mean()
)
