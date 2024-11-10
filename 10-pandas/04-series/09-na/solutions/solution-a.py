
result = (
    pd.Series(DATA)
      .fillna(0, limit=1)
      .dropna()
      .reset_index(drop=True)
)
