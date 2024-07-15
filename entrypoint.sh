#!/bin/bash
set -e

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing"

python manage.py migrate

python manage.py collectstatic --noinput

python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(username='admin', password='admin', email='admin@admin.com') if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists() else None"

exec "$@"
