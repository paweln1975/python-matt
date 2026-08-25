import time

class DatabaseQuery:
    def execute(self, query):
        # Simulate a time-consuming database query
        return f"Results for '{query}'"

class RealDatabaseQuery(DatabaseQuery):
    def execute(self, query):
        print(f"Executing query: {query}")
        return super().execute(query)

class CacheProxy(DatabaseQuery):
    def __init__(self, real_database_query, cache_duration_seconds=5):
        self._cache = {}
        self.real_query = real_database_query
        self.cache_duration_seconds = cache_duration_seconds

    def execute(self, query):
        if query in self._cache and (time.time() - self._cache[query]["timestamp"] < self.cache_duration_seconds):
            print(f"Cache hit for query: {query}")
            return self._cache[query]["result"]
        else:
            print(f"Cache miss for query: {query}. Executing real query.")
            result = self.real_query.execute(query)
            self._cache[query] = {"result": result, "timestamp": time.time()}
            return result

if __name__ == "__main__":
    real_query = RealDatabaseQuery()
    proxy = CacheProxy(real_query, cache_duration_seconds=5)

    # First execution (cache miss)
    print(proxy.execute("SELECT * FROM users"))

    # Second execution (cache hit)
    print(proxy.execute("SELECT * FROM users"))

    # Wait for cache to expire
    time.sleep(6)

    # Third execution (cache miss after expiration)
    print(proxy.execute("SELECT * FROM users"))

    # Fourth execution (cache hit)
    print(proxy.execute("SELECT * FROM users"))