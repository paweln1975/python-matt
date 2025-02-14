from django.core.exceptions import ImproperlyConfigured
from pathlib import Path

SECRET_KEY_FILE = Path('../secret-key.txt')

if not SECRET_KEY_FILE.exists():
    raise ImproperlyConfigured('SECRET_KEY file does not exist')

SECRET_KEY = SECRET_KEY_FILE.read_text().strip()

if not SECRET_KEY:
    raise ImproperlyConfigured('SECRET_KEY is empty')