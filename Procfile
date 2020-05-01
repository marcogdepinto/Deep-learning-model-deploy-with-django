web: gunicorn DjangoRestDeepLearning.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
release: manage.py makemigrations App
release: manage.py migrate App
