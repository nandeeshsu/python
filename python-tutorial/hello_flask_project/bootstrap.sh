#!/bin/sh

#To run the local debug server 
#export FLASK_APP=./hello/index.py
#pipenv run flask --debug run -h 0.0.0.0

#To run the wsgi server gunicorn in production
#https://dev.to/brandonwallace/deploy-flask-the-easy-way-with-gunicorn-and-nginx-jgc
#https://webdock.io/en/docs/how-guides/app-installation-and-setup/how-setup-python-web-application-flask-gunicorn-and-nginx
pipenv run gunicorn --workers 4 --bind 0.0.0.0:5000 hello.wsgi:app