
df['type'] = pd.cut(df['consumption'],
                    bins=[0, 1, 10, np.inf],
                    labels=['electric', 'car', 'tir'],
                    include_lowest=True)

old = df['mileage'] > 100_000
young = df['mileage'].between(10_000, 100_000)
new = df['mileage'].between(0, 10_000)

df['status'] = pd.NA
df.loc[old, 'status'] = 'old'
df.loc[young, 'status'] = 'young'
df.loc[new, 'status'] = 'new'

result = df.describe()

# Extra Task
plot = df.hist(rwidth=0.8, figsize=(17, 5))
df.groupby(['type', 'status']).describe()
df.groupby(['type', 'status']).describe().transpose()


#%% Alternative Solution
# young = df['mileage'] >= 10_000 & df['milage'] <= 100_000
# young = df['mileage'].isin(np.arange(10_000, 100_000))
