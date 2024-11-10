
s = pd.Series(
    data=np.random.randn(100),
    index=pd.date_range('2000-01-01', freq='D', periods=100),
)


result = {
    '2000-02-29': s.loc['2000-02-29'],
    'first': s.iloc[0],
    'last': s.iloc[-1],
    'middle': s.iloc[s.size // 2],
}
