## File: myproject/middleware.py
from time import time


class MyMiddleware:
    def __init__(self, get_response):
        """Called once, when the server starts"""
        self.get_response = get_response
        print('init')

    def __call__(self, request):
        """Called for each request"""
        start = time()
        response = self.get_response(request)
        stop = time()
        duration = stop - start
        print(f'Processing time: {duration:.2f}')
        print(request)
        print(response)
        return response