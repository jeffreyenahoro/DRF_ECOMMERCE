from .base import *

SECRET_KEY = os.environ.get("LOCAL_SECRET_KEY")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
