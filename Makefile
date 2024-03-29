test: runflake
	python manage.py test --settings=baran.settings.test
runflake:
	@flake8 ./ --exclude='*venv,*venv_*,**migrations*,*settings*,*flake8*,manage.py,wsgi.py,wsgi-beta.py,__init__.py,*node_modules*, *LC_MESSAGES*' --ignore=E125,W605,W503
install-base:
	pip install -r ./requirements/base.txt
install-development:
	pip install -r ./requirements/development.txt
install-heroku:
	pip install -r ./requirements/heroku.txt
migrate:
	python manage.py migrate --settings=baran.settings.development
create-demo-user:
	python manage.py create_demo_user
import-employees-data:
	python manage.py import_employees_data
populate-db: migrate create-demo-user import-employees-data

install: install-base
install-dev: install-development
install-prod: install-heroku
