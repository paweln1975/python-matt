

def clean(text: str) -> str:
    return (
        text

        # Normalize
        .upper()
        .strip()

        # Remove whitespaces
        .replace('\t', ' ')
        .replace('\n', ' ')
        .replace('    ', '')
        .replace('   ', '')
        .replace('  ', '')

        # Remove special characters
        .replace('.', '')
        .replace('\\', '')
        .replace('-', '')
        .replace('|', '')
        .replace('(', '')
        .replace(')', '')

        # Remove text
        .removeprefix('ULICA')
        .removeprefix('UL')

        # Replace
        .replace('3', 'III')
        .replace('2', 'II')
        .replace('1', 'I')
        .replace('TRZECIEGO', 'III')
        .replace('DRUGIEGO', 'II')
        .replace('PIERWSZEGO', 'I')

        # Format
        .title()
        .replace('Iii', 'III')
        .replace('Ii', 'II')
        .strip()
    )



result = pd.Series(DATA).apply(clean)
