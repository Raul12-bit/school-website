#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python compile_locales.py
python manage.py collectstatic --no-input
python manage.py migrate --no-input
