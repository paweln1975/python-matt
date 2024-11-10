
def myfunc(cell):
    if not isinstance(cell, dict):
        return pd.NA
    if 'summary' not in cell:
        return pd.NA
    return cell['summary']


resp = requests.get(DATA)
data = resp.json()['paths']

result = (
    pd
    .DataFrame(data)
    .transpose()
    .map(myfunc)
)
