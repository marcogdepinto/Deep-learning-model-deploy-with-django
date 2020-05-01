web: gunicorn DjangoRestDeepLearning.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
release: python manage.py makemigrations App
release: python manage.py migrate App
