#!/bin/sh

set -e

if [ "$DEBUG" = "True" ]; then
    export DJANGO_SETTINGS_MODULE=server.settings.development
    python manage.py migrate --no-input
    # 와이파이 IP로 변경 필요
    # python manage.py runserver 0.0.0.0:8000
    python manage.py runserver 192.168.219.161:8000
    
else
    export DJANGO_SETTINGS_MODULE=server.settings.production
    
    python manage.py collectstatic --noinput
    python manage.py migrate --no-input
    gunicorn server.wsgi:application --bind 0.0.0.0:8000
fi