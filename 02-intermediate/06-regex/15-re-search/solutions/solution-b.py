
pattern = r'<p>(We choose .+?)</p>'
result = re.search(pattern, DATA, flags=re.DOTALL).group(1)
