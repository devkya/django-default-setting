from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "movie-development-db",
        "USER": "xpert",
        "PASSWORD": "1q2w3e!Q",
        "HOST": "prod-db",
        "PORT": "5432",
    }
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("prod-redis", 6379)],
        },
    },
}
