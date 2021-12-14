test: runflake
	python manage.py test --settings=brana.settings.test
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
create-system-user:
	python manage.py create_system_user

install: install-base migrate create-system-user
install-dev: install-development migrate create-system-user
install-prod: install-heroku migrate create-system-user
