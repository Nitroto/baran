# Baran Simple Emploee application

## Tech stack

### Backend

- [Python 3.9](https://www.python.org/)
- [Django 2.2.25](https://www.djangoproject.com/)
- [Django REST Framework 3.13.0](https://www.django-rest-framework.org/)
- [Django REST Swagger 2.2.0](https://django-rest-swagger.readthedocs.io/)

### Web

- [Vue 3](https://vuejs.org/)
- [TypeScript](https://www.typescriptlang.org/)

## Instructions

### Set environment variables

- `SECRET_KEY` - Create one with:
    ```
    $ python
    >>> from django.core.management.utils import get_random_secret_key
    >>> get_random_secret_key()
    ```
- `DEBUG` - Default value False for Development environment should be True
- `ALLOWED_HOSTS` - add allowed hosts, default is empty
  list. [Django documentation](https://docs.djangoproject.com/en/2.2/ref/settings/#allowed-hosts)
- `SSL_REQUIRE` - Default value True for Development environment should be False

.env file can be used, put it in settings folder `baran/settings`

### Running locally

Backend Django server (port 8000):  
`$ python manage.py runserver --settings=baran.settings.development`

Frontend Svelte server (port 8080):  
`$ cd frontend/web`  
`$ npm run dev`
