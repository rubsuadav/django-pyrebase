#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
pip install -U drf-yasg
pip install whitenoise[brotli] 

python manage.py collectstatic --no-input