from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "movie-development-db",
        "USER": "xpert",
        "PASSWORD": "1q2w3e!Q",
        "HOST": "db",
        "PORT": "5432",
    }
}
