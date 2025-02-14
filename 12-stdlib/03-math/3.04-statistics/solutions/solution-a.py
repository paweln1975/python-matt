def stats(values):
    return {
        'mean': mean(values),
        'stdev': stdev(values),
        'median': median(values),
        'variance': variance(values),
    }