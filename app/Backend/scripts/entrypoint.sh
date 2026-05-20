#!/usr/bin/env sh
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput

if [ "${SEED_DATA:-true}" = "true" ]; then
  python manage.py seed_data --productos "${SEED_PRODUCTOS:-1000}" --pedidos "${SEED_PEDIDOS:-3000}"
fi

exec "$@"
