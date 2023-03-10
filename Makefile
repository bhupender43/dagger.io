# Set the path to your virtual environment
VENV_PATH = venv

# Set the name of your Django application
DJANGO_APPLICATION_NAME = webapp

# Set the number of worker processes to use with Gunicorn
GUNICORN_WORKERS = 2

# Set the port number that Gunicorn will listen on
GUNICORN_PORT = 8000

# Start the Django development server
run:
	source $(VENV_PATH)/bin/activate && python manage.py runserver

# Run database migrations
migrate:
	source $(VENV_PATH)/bin/activate && python manage.py makemigrations && python manage.py migrate

# Stop the Gunicorn server
stop:
	kill `cat gunicorn.pid`

# Start the Gunicorn server
start:
	source $(VENV_PATH)/bin/activate && gunicorn $(DJANGO_APPLICATION_NAME).wsgi:application --workers $(GUNICORN_WORKERS) --bind 127.0.0.1:$(GUNICORN_PORT)  --daemon --pid gunicorn.pid

# Restart the Gunicorn server
restart: stop start
