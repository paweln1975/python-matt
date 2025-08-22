import json
import csv

input_file = 'checker-properties.json'
output_file = 'checker_output.csv'

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['checker_name', 'type', 'impact', 'language', 'rule_strength'])
    for checker in data:
        name = checker.get('checkerName', '')
        checker_type = checker.get('type', '')
        impact = checker.get('impact', '')
        language = checker.get('language', '')
        rule_strength = checker.get('ruleStrength', '')
        if not language:
            families = checker.get('families', [])
            if isinstance(families, list):
                language = ','.join(families)
        writer.writerow([name, checker_type, impact, language, rule_strength])