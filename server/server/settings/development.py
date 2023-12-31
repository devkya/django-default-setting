from .base import *

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, "env", "development.env"))
DEBUG = True

ALLOWED_HOSTS = ["*"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "movie-development-db",
        "USER": "xpert",
        "PASSWORD": "1q2w3e!Q",
        "HOST": "dev-db",
        "PORT": "5432",
    }
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("dev-redis", 6379)],
        },
    },
}
