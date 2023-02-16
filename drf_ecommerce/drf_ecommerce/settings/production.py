from .base import *



SECRET_KEY = os.environ.get("PRODUCTION_SECRET_KEY")


ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}