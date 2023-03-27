install:
	poetry install

lint:
	poetry run flake8

black:
	poetry run black .

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

mm:
	python3 manage.py makemigrations
	python3 manage.py migrate

.PHONY: install lint black makemigrations migrate