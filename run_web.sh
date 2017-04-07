#!/bin/sh
# wait for PSQL server to start

python manage.py migrate
gunicorn -w 4 --bind 0.0.0.0:8000 farma.wsgi:application