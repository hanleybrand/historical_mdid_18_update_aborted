# Madison Digial Image Database (MDID)

The [Madison Digital Image Database](http://mdid.org/) is a free, open source media repo aimed at education spaces.
It was created at [James Madison University](http://www.jmu.edu).

## Django 1.6.5 upgrade - clone to a new directory

**Status:** Currently in a "first running" state - will work on an existing mdid3 installation's database, although obvs don't run it against a production database.

**This branch has the potential to mess up the organization of a django 1.2.7 based branch, so it seems best to `git clone` to seperate directory**

I'm currently running it on OS X but I tried to make any settings changes as generic as possible (I made most if not all directories set relative to PROJECT_ROOT

### setting up

I'd recommend making a fresh virtual env with python 2.7.x so everything has that 'oh-so-fresh' feeling!

I've been developing/testing this fork with an export of a production database and I haven't hit a snag, so right on!

- Switched static files to the staticfiles app, so a good start for running against an already existing database after setting up your virtualenv is:
``` shell 
pip install -f requirements.txt
python manage.py collectstatic
python manage.py runserver
``` 
- Following the newer django convention, moved the main app files to a 'project' directory, and followed [Jeff Knupp's advice](http://www.jeffknupp.com/blog/2013/12/18/starting-a-django-16-project-the-right-way/) that this is really a 'config' directory, so settings file plus the main urls & wsgi files are in the PROJECT_ROOT/config directory, collected staticfiles are in PROJECT_ROOT/static, and local templates are in PROJECT_ROOT/templates.

