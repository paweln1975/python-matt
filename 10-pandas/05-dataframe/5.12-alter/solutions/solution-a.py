new = df['mileage'].between(0, 10_000)
young = df['mileage'].between(10_000, 100_000)
old = df['mileage'].between(10_000, 1_000_000)

df['status'] = pd.NA
df.loc[old, 'status'] = 'old'
df.loc[young, 'status'] = 'young'
df.loc[new, 'status'] = 'new'

result = df