#!/bin/bash
while [ ! -f "/is_ready/yes" ]; do
    sleep 1
done
rm -f /is_ready/yes
python manage.py makemigrations
python manage.py migrate
echo "RUN SERVER"
python manage.py runserver 0.0.0.0:8000