Getting started
===============

Installation
------------

Python Version
^^^^^^^^^^^^^^

It's recommended to use the latest version of Python. Domum supports Python 3.8 and newer.

Download Domum
^^^^^^^^^^^^^^

You can get the latest development version from `Github <https://github.com/SvenKortekaas04/domum>`_.

Install requirements
^^^^^^^^^^^^^^^^^^^^

After downloading and unpacking it, you will have to install a few requirements for Domum to run smoothly. You can install all the requirements using::

$ pip install -r requirements.txt

Initialize a database
^^^^^^^^^^^^^^^^^^^^^

Domum requires a database to store additional data. To create a new database, run the following command::

$ python manage.py migrate

Demonstration
^^^^^^^^^^^^^

Let's verify that Domum is working. Run the following command::

$ python manage.py runserver

Now that the server is running, go to http://127.0.0.1:8000/ in the browser.