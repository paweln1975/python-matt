
result = pd.read_html(DATA, header=0)[0]
result = result.head(146).tail(11)

with sqlite3.connect(FILE) as db:
    result['Event'].to_sql('apollo11', db)
