.PHONY: help dryrun docker-build docker-run tests install-requirements

help:
	@echo "    dryrun"
	@echo "        Run project in development mode."
	@echo "    docker-build"
	@echo "        Prepare docker container for project."
	@echo "    docker-run"
	@echo "        Run docker container."
	@echo "    tests"
	@echo "        Run unit tests."
	@echo "    install-requirements"
	@echo "        Install dependencies from requirements.txt"

dryrun:
	cd benchmark/ && python batch.py
	cd benchmark/ && gunicorn --workers=4 --bind 0.0.0.0:5000 wsgi:app

docker-build:
	docker build . -t bench-{{cookiecutter.project_name}}

docker-run:
	docker run -p 5000:5000 --mount type=bind,source=$(shell pwd)/logs,target=/root/logs --name bench-{{cookiecutter.project_name}} bench-{{cookiecutter.project_name}}

tests:
	cd benchmark/ && python -m pytest

install-requirements:
	pip install -r requirements.txt
