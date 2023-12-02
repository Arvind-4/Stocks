#!/bin/bash

echo "Installing Python sqlite3..."
cd /usr/local/bin/
yum install sqlite-devel -y
./configure --enable-optimizations --enable-loadable-sqlite-extensions
make && make altinstall
cd /vercel/path0/

echo "Upgrade pip..."
python3.9 -m pip install --upgrade pip

echo "Installing dependencies..."
python3.9 -m pip install -r requirements.txt

echo "Migrating database..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Creating superuser..."

DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}

python3.9 manage.py createsuperuser \
    --email $DJANGO_SUPERUSER_EMAIL \
    --noinput || true

echo "Collecting static files..."
python3.9 manage.py collectstatic  --noinput --clear