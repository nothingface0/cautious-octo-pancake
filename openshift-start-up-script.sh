#!/bin/bash

python manage.py collectstatic --noinput
python manage.py migrate --run-syncdb

daphne -b 0.0.0.0 -p 8080 django_test.asgi:application
# gunicorn --bind=0.0.0.0:8080 mlp.wsgi
# python manage.py runserver 0.0.0.0:8080
