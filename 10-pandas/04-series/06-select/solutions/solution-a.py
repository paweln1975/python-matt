
s = pd.Series(
    data=np.random.randn(100),
    index=pd.date_range('2000-01-01', freq='D', periods=100))

result = {
    'head': s.head(1),
    'tail': s.tail(5),
    'first': s.first('2W'),
    'last': s.last('M'),
    'sample_n': s.sample(n=3),
    'sample_frac': s.sample(frac=1.25, replace=True),
}
