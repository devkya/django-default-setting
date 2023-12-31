#!/bin/sh

set -e

if [ "$DEBUG" = "True" ]; then
    export DJANGO_SETTINGS_MODULE=server.settings.development
    python manage.py migrate --no-input
    # 로컬망에서 접속 가능한 개발 서버 실행
    python manage.py runserver 0.0.0.0:8000
    
    
else
    export DJANGO_SETTINGS_MODULE=server.settings.production
    
    python manage.py collectstatic --noinput
    python manage.py migrate --no-input
    gunicorn server.wsgi:application --bind 0.0.0.0:8000
fi