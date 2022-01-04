# Baran Simple Employee application

## Tech stack

### Backend

- [Python 3.10](https://www.python.org/)
- [Django 4.0.1](https://www.djangoproject.com/)

## Instructions

### Set environment variables

- `SECRET_KEY` - Create one with:
    ```
    $ python
    >>> from django.core.management.utils import get_random_secret_key
    >>> get_random_secret_key()
    ```
- `DEBUG` - Default value False for Development environment should be True
- `ALLOWED_HOSTS` - add allowed hosts, default is empty list. [Django documentation](https://docs.djangoproject.com/en/2.2/ref/settings/#allowed-hosts)

.env file can be used, put it in settings folder `baran/settings`

### Running locally

Backend Django server (port 8000):  
`$ make install` - for install base dependencies  
`$ make install-dev` - for install base and development dependencies  
`$ make populate-db` - migrate, create demo user and import employees from xlsx file  
`$ python manage.py runserver --settings=baran.settings.development` - run development server

### [Demo application](https://simpleemployee.herokuapp.com/)
