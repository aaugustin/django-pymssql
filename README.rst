django-pymssql
==============

Goals
-----

django-pymssql is a Django database backend for Microsoft SQL Server that
works on non-Windows systems.

It's a small wrapper around django-mssql_ that uses pymssql_ instead of ADO to
connect to SQL Server.

It should support the same versions of Python, Django and SQL Server as
django-mssql_.

The original use case was to connect to SQL Server from a Django project
written in Python 3 and running on Linux.

Status
------

django-pymssql 1.7 almost_ passes Django's test suite with:

- Python 2.7 or 3.4
- Django 1.7.x + django-mssql 1.6.1 + pymssql 2.1.1
- Microsoft® SQL Server® 2012 Express

Usage
-----

django-pymssql provides a Django database engine called ``sqlserver_pymssql``:

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'sqlserver_pymssql',
            'HOST': '...',
            'NAME': '...',
            'USER': '...',
            'PASSWORD': '...','
            'OPTIONS': {
                # ...
            },
        },
    }

Any parameter accepted by `pymssql.connect`_ can be passed in OPTIONS.

Alternatives
------------

django-sqlserver_ is a fork of django-mssql_ that supports python-tds_ and
pymssql_ in addition to ADO on Windows. Unfortunately it has diverged and it
lags behind django-mssql_ when it comes to supporting newer Django versions.

django-pyodbc_ relies on pyodbc_ to connect to SQL Server. It requires a
complex stack that doesn't bring actual benefits. Besides it doesn't appear
to be very mature nor actively maintained.

Hacking
-------

Clone Django, pymssql, django-mssql and django-pymssql and ``pip install -e
.`` each of them in a virtualenv.

Create a Django tests settings file with the database engine set to
``'sqlserver_pymssql'`` and credentials for a testing SQL Server instance.

Go the the ``tests`` subdirectory in a clone of Django and execute
``./runtests.py --settings=test_pymssql``.

License
-------

django-pymssql is released under the MIT license, like django-mssql_. See the
LICENSE file for details. Note that pymssql_ is released under the LGPL.

Some database version checking code was borrowed from django-sqlserver_ which
is also released under the MIT license..

.. _almost: https://github.com/aaugustin/django-pymssql/search?q=failing_tests
.. _django-mssql: http://django-mssql.readthedocs.org/
.. _django-pyodbc: https://github.com/lionheart/django-pyodbc
.. _django-sqlserver: https://github.com/denisenkom/django-sqlserver
.. _pymssql: http://www.pymssql.org/
.. _pymssql.connect: http://pymssql.org/en/latest/ref/pymssql.html#pymssql.connect
.. _pyodbc: https://github.com/mkleehammer/pyodbc
.. _python-tds: https://github.com/denisenkom/pytds
