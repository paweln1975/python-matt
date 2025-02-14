with sqlite3.connect(FILE) as db:
    result['Event'].to_sql('apollo11', db)