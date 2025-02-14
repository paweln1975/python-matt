def extract(column: pd.Series):
    if type(column) is dict:
        return column.get('summary')
    return pd.NA


result = (
    pd
    .DataFrame(data)
    .transpose()
    .map(extract)
)