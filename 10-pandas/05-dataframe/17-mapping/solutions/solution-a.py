
result = pd.read_csv(DATA, parse_dates=['datetime'])
result['date'] = result['datetime'].dt.date
result['time'] = result['datetime'].dt.time


#%% Alternative Solution
# result = pd.read_csv(DATA, parse_dates=['datetime'])
# result['date'] = result['datetime'].map(lambda dt: dt.date())
# result['time'] = result['datetime'].map(lambda dt: dt.time())


#%% Alternative Solution
# result = pd.read_csv(DATA, parse_dates=['datetime'])
# result[['date', 'time']] = result['date'].map(str).str.split(expand=True)
