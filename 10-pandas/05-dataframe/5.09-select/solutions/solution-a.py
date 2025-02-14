df = pd.read_csv(DATA)
query = df['petal_length'] > 2.0
result = df[query].head(5)