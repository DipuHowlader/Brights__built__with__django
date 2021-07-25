#### A web-agency website, developed with Django as full-stack

It's a web application written with Django as a full-stack.

## System Requirements

* Python 3.9.5
* Django 3.2.3

## installation

1. Clone this repository: `https://github.com/DipuHowlader/Brights_django.git`:

2. Create a Python 3.9 virtualenv `virtualenv env`

3. Active virtualenv(for linux):
	`source env/Scripts/activate`
	
4. Install dependencies:
	`pip install -r requirements.txt`
	
5. create Migrations `python manage.py makemigrations`

6. Migrate Database `python manage.py migrate`

7. Create Super User `python manage.py createsuperuser`

8. Finally Run The Project `python manage.py runserver`
