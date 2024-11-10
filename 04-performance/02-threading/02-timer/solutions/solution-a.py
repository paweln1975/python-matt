
def ping(n: int = 1):
    result.append(n)
    if n < MAX:
        Timer(INTERVAL, ping, [n + 1]).start()
