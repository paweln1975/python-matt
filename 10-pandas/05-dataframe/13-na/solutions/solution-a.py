
class_labels = pd.read_csv(DATA, nrows=0).columns[2:]
label_encoder = dict(enumerate(class_labels))

result = (
    pd.read_csv(DATA, skiprows=1, names=COLUMNS)
      .replace({'species': label_encoder})
)

query = result['petal_length'] < 4
result.loc[query, 'petal_length'] = np.nan
result = result.interpolate('linear')
result = result.dropna(how='any', axis='rows')
result = result.head(n=2)
