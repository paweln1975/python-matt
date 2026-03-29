import os
import requests  # Assuming requests library is available for actual HTTP calls
import logging
from datetime import timedelta, datetime
import json

"""
Gateway Pattern Example in Python

The Gateway pattern provides a single entry point to a subsystem, encapsulating the complexity
of interacting with external systems or services. It acts as a facade, simplifying the interface
for clients and allowing for easier maintenance, testing, and changes to the underlying systems.

In this example, we implement a simple APIGateway that handles HTTP requests to an external API.
"""

logging.basicConfig(
        level=logging.INFO,
        format='"%(asctime).19s", "%(levelname)s", "%(message)s"'
)
log = logging.getLogger(__name__)

class Cache:
    def __init__(self, expiration:timedelta = timedelta(seconds=10), location:str ='') -> None:
        self.expiration = expiration
        self.location = location

    def get(self, key: str):
        raise NotImplementedError()

    def set(self, key: str, value: str):
        raise NotImplementedError()

    def is_valid(self, key: str) -> bool:
        raise NotImplementedError()

class FileSystemCache(Cache):
    def __init__(self, location='tmp', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.location = location

    def __get_cache_path(self, key: str) -> str:
        filename = key.replace('/', '_').replace(' ', '_').replace('-', '_')
        return os.path.join(self.location, filename)

    def set(self, key: str, value: str):
        filename = self.__get_cache_path(key)

        if not os.path.isdir(self.location):
            os.makedirs(self.location)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(value)

    def get(self, key: str):
        filename = self.__get_cache_path(key)

        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()

    def is_valid(self, key: str) -> bool:
        filename = self.__get_cache_path(key)

        try:
            last_modified = os.path.getmtime(filename)
            last_modification_time = datetime.fromtimestamp(last_modified)
            now = datetime.now()
            if now - last_modification_time < self.expiration:
                return True
        except FileNotFoundError:
            pass
        return False



class APIGateway:
    def __init__(self, base_url: str, api_key: str = None, cache: Cache = None):
        self.base_url = base_url
        self.api_key = api_key
        self.cache = cache
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})

    def get(self, endpoint: str) -> dict:
        """
        Perform a GET request to the API.
        """
        url = f"{self.base_url}{endpoint}"
        key = endpoint
        
        if self.cache and self.cache.is_valid(key):
            try:
                cached_data = self.cache.get(key)
                log.info(f"Got cached data: {cached_data}")
                return json.loads(cached_data)
            except (FileNotFoundError, json.JSONDecodeError):
                pass  # Proceed to fetch
        
        response = self.session.get(url)
        response.raise_for_status()
        data = response.json()
        log.info(f"Fetched data from API: {data}")

        if self.cache:
            self.cache.set(key, json.dumps(data))
        
        return data

# Example usage
if __name__ == "__main__":
    # Simulate a gateway to a fictional API
    cache = FileSystemCache(location='tmp')
    gateway = APIGateway("https://python3.info", cache=cache)

    # Get user data
    user_data = gateway.get("/_static/myusers.json")
    for user in user_data:
        log.info(f"User: {user['firstname']} {user['lastname']} {user['email']}")
