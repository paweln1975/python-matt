df['type'] = pd.cut(
    x=df['consumption'],
    bins=[0, 1, 10, 100],
    labels=['electric', 'car', 'truck'],
    include_lowest=True,
)

result = df