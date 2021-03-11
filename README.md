# Djangocoockiecutter

Django-coockiecutter desc

## Quickstart

1. Install requirements:

        pipenv install

2. Create `.env` configuration file based on `env.sample`:

        cp env.sample .env
        vim .env

   *Note*: you'll need to create the database and set `DATABASE_URL` in
   the configuration file before you can run migrations and use the code.

3. Run migrations:

        pipenv run python manage.py migrate

4. Run the server:

        pipenv run python manage.py runserver

5. Visit the browsable API at http://localhost:8000/api/v1/

6. Access the Django admin at http://localhost:8000/admin/

## Creating superuser

A superuser account can be created using the Django management command:

    pipenv run python manage.py createsuperuser

## Running tests

    pipenv run python manage.py test

