
result = map(datetime.fromisoformat, DATA)

#%% Alternative Solution
result = [datetime.fromisoformat(x) for x in DATA]
