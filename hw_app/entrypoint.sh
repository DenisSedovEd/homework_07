#!/bin/sh

set -e

echo "Apply alembic migrations"

alembic upgrade head

#python api_calls.py

echo "Successfully alembic migrations"

exec "$@"