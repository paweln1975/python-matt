
header, *rows = DATA
*attributes, _ = header


for *measurements, species in rows:
    if species not in result:
        result[species] = dict()
    for i, column in enumerate(attributes):
        if column not in result[species]:
            result[species][column] = dict(values=[])
        result[species][column]['values'].append(measurements[i])


for species, attributes in result.items():
    for attribute_name in attributes.keys():
        values = result[species][attribute_name]['values']
        result[species][attribute_name]['mean'] = mean(values)
        result[species][attribute_name]['median'] = median(values)
        result[species][attribute_name]['stdev'] = stdev(values)
        result[species][attribute_name]['variance'] = variance(values)
