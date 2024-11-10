
header, *lines = DATA.splitlines()
nrows, nvalues, *class_labels = header.strip().split(',')
result = dict(enumerate(class_labels))
