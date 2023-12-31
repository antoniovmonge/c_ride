# c_ride

Rides for everyone!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Local Development: Set the environment variable `COMPOSE_FILE` pointing to `local.yml`

```bash
set COMPOSE_FILE=local.yml
```

```bash
docker compose up --build
```

```bash
docker compose down
```

```bash
docker compose down -v
```

```bash
docker compose ps
```

#### Execute Management Commands

```bash
docker compose -f local.yml run --rm django python manage.py makemigrations
```

```bash
docker compose -f local.yml run --rm django  python manage.py migrate
```

### Open the shell

```bash
docker-compose -f local.yml run --rm django python manage.py shell_plus
```

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

```bash
docker compose run --rm django python manage.py createsuperuser
```

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

```bash
mypy c_ride
```

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

```bash
docker-compose -f local.yml run --rm django coverage run -m pytest
```

```bash
docker-compose -f local.yml run --rm django coverage html
```

```bash
docker-compose -f local.yml run --rm django open htmlcov/index.html
```

#### Running tests with pytest

```bash
docker-compose -f local.yml run --rm django run -m pytest
```

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Celery

This app comes with Celery.

To run a celery worker:

```bash
cd c_ride
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the same folder with _manage.py_, you should be right.

To run [periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), you'll need to start the celery beat scheduler service. You can start it as a standalone process:

```bash
cd c_ride
celery -A config.celery_app beat
```

or you can embed the beat service inside a worker with the `-B` option (not recommended for production use):

```bash
cd c_ride
celery -A config.celery_app worker -B -l info
```

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [Mailpit](https://github.com/axllent/mailpit) with a web interface is available as docker container.

Container mailpit will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With Mailpit running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

### Debugging

Stop only the django container with the following command:

```bash
docker compose ps
```

Select the django container id and run the following command:

```bash
docker rm -f c_ride_local_django
```

Run the django container with the following command:

```bash
docker compose run --rm --service-ports django
```

Add in the code the following line:

```python
import ipdb; ipdb.set_trace()
```

### Code Quality

```bash
docker-compose -f local.yml run --rm django black .
```

```bash
pre-commit run --all-files
```

### Create Local User and Admin

```bash
docker-compose -f local.yml run --rm django python manage.py create_local_user_and_admin
```

### Load Data for Circles

```bash
docker-compose -f local.yml run --rm django python manage.py loaddata c_ride/circles/fixtures/circles.json
```
