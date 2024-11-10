
for paragraph in re.finditer(PATTERN, DATA):
    text = paragraph.group(1)
    if text.startswith('We choose'):
        result = text
