result = (pd
    .read_csv(DATA, parse_dates=['datetime'])
    .assign(
        date=lambda df: df['datetime'].dt.date,
        time=lambda df: df['datetime'].dt.time,
    )
)