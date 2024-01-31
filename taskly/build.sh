#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r taskly/requirements.txt

python taskly/manage.py collectstatic --no-input
python taskly/manage.py migrate