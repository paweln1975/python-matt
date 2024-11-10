
paragraph = re.compile(r'</?p>')

for p in paragraph.split(DATA):
    if p.startswith('We choose to go to the moon'):
        result = p
