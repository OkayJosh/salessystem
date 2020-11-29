python sales/manage.py migrate
gunicorn sales.sales.wsgi:application --bind 0.0.0.0:8000 --log-level info --timeout 180  --workers 3
