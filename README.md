# Python: Getting Started

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:bertrandrafael/marvel-api-django.git
$ cd marvel-api-django

$ git remote add origin git@github.com:heroku/your-repository.git

$ pip install -r requirements.txt

$ createdb marvel-api-django

$ python manage.py migrate
$ python manage.py collectstatic

Put your Public and Privante key in marvel/views.py

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

Or other port:
$ heroku local -p 5002

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
