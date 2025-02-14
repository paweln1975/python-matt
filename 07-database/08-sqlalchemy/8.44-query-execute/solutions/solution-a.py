engine = create_engine('sqlite:////tmp/space.db')
Model = declarative_base()

query = text("""
    SELECT *
    FROM sqlite_master
""")

with engine.connect() as db:
    result = db.execute(query).all()
    print(result)