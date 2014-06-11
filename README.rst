.. image:: http://www.gravatar.com/avatar/089181cf39900bb836059b0b2c0e9b98?s=128

====================
MegaProjects Website
====================

A construction project is a story, researched by the architect, actualised by
the engineer and told by us.

Working Environment
===================

You have several options in setting up your working environment. We recommend
using virtualenv to separate the dependencies of your project from your system's
python environment. If on Linux or Mac OS X, you can also use pyenv to help
manage multiple virtualenvs across different projects.

virtualenv Only
---------------

First, make sure you are using virtualenv (http://www.virtualenv.org). Once
that's installed, create your virtualenv::

    $ virtualenv --distribute megaprojects

You will also need to ensure that the virtualenv has the project directory
added to the path. Adding the project directory will allow `django-admin.py` to
be able to change settings using the `--settings` flag.

virtualenv with pyenv
---------------------

In Linux and Mac OSX, you can install pyenv (http://github.com/yyuu/pyenv-installer),
which will take care of managing your virtual environments::

    $ pyenv install PYTHON_VERSION
    $ pyenv virtualenv PYTHON_VERSION megaprojects
    $ pyenv activate megaprojects

Installation of Dependencies
============================

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*
