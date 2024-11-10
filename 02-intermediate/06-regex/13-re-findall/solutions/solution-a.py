
year = r'(?P<year>\d{4})'
month = r'(?P<month>[A-Z][a-z]+)'
day = r'(?P<day>[0-9]{1,2})'
pattern = f'{month}\s+{day},\s+{year}'
result = re.findall(pattern, DATA, flags=re.MULTILINE)
