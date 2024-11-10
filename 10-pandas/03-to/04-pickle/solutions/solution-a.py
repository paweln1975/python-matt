
df = (pd
  .read_html(DATA, header=0)[0]
  .head(n=146)
  .tail(n=11)
)

df['Event'].to_pickle(FILE)
