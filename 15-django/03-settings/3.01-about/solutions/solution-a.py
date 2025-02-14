from os import getenv

DEBUG = bool(getenv('DJANGO_DEBUG', default=False))