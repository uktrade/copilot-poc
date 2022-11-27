web: python manage.py migrate && python manage.py load_defaults && gunicorn -b 0.0.0.0:$PORT demodjango.wsgi:application
