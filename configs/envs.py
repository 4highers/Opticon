"""Place to keep environment variables."""

from os import environ

HOST: str = environ.get('HOST', '0.0.0.0')
PORT: int = int(environ.get('PORT', 8080))
LOG_LEVEL: str = environ.get('LOG_LEVEL', 'INFO').upper()
BASE_PATH: str = environ.get('BASE_PATH', '')
DEBUG: bool = environ.get('DEBUG', None) is not None
