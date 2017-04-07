#!/bin/sh
# esperamos por la db
sleep 5
cd web/django_app/
python manage.py migrate
gunicorn -w 4 --bind 0.0.0.0:8000 farma.wsgi:application