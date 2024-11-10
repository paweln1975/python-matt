
def translate(cell):
    return ''.join(LETTERS_PLEN.get(x,x) for x in cell)

result = (
    pd
    .read_excel(DATA, sheet_name='Polish', header=1, index_col=0)
    .map(translate)
    .rename(translate, axis='columns')
)
