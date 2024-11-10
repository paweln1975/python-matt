
resp = requests.get(DATA)
data = resp.json()['paths']
result = pd.DataFrame(data)
