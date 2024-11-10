
class_labels = pd.read_csv(DATA, nrows=0).columns[2:]
label_encoder = dict(enumerate(class_labels))

result = (pd
    .read_csv(DATA, names=COLUMNS, skiprows=1, nrows=25)
    .replace({'label': label_encoder})
)
