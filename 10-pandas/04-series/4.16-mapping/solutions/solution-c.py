def clean(text: str) -> str:
    return (
        text

        # Normalize string
        .upper()
        .strip()

        # Normalize whitespace
        .replace('\t', ' ')
        .replace('    ', ' ')
        .replace('   ', ' ')
        .replace('  ', ' ')

        # Remove escape characters
        .replace('\r', '')
        .replace('\n', '')
        .replace('\f', '')
        .replace('\v', '')
        .replace('\b', '')

        # Remove special characters
        .replace('.', '')
        .replace(',', '')
        .replace(';', '')
        .replace('|', '')

        # Remove prefixes
        .removeprefix('ULICA')
        .removeprefix('OSIEDLE')
        .removeprefix('ALEJA')
        .removeprefix('PLAC')
        .removeprefix('UL')
        .removeprefix('OS')
        .removeprefix('AL')
        .removeprefix('PL')

        # Replace fragments
        .replace('TRZECIEGO', 'III')
        .replace('DRUGIEGO', 'II')
        .replace('PIERWSZEGO', 'I')
        .replace('3', 'III')
        .replace('2', 'II')
        .replace('1', 'I')

        # Format output
        .strip()
        .title()
        .replace('Iii', 'III')
        .replace('Ii', 'II')
    )


result = pd.Series(DATA).apply(clean)