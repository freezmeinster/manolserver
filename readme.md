# Manol Server

## Prerequest
* Python 2.7
* Ubuntu 16.04

## Installation 
* Clone Source code.
* Create Virtualenv.
* Install dependency: `pip install -r requirements.txt`.
* Create database: `python manage.py migrate`.
* Create Superuser `python manage.py createsuperuser`.
* Done.

## Startup
* Get into virtualenv.
* Execute `python manage.py runserver`.
   Manol will powerup development server with websockets support.