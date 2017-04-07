#!/bin/sh

# wait for RabbitMQ server to start

sleep 5
cd web/django_app

celery -A farma worker -l info

