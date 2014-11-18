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

The original use case was to connect to SQL Server from a Django projet
written in Python 3 and running on Linux.

Status
------

As of June 5th, 2014, django-pymssql almost_ passes Django's test suite with:

- Python 2.7
- The stable/1.7.x branch of Django
- The development version of pymssql
- The development version of django-mssql

Usage
-----

django-pymssql provides a Django database engine called ``sqlserver_pymssql``::

    DATABASES = {
        'default': {
            'ENGINE': 'sqlserver_pymssql',
            'HOST': '...',
            'NAME': '...',
            'USER': '...',
            'PASSWORD': '...','
            'OPTIONS': {
                #
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
complex stack which doesn't bring actual benefits. Besides it doesn't appear
to be very mature nor actively maintained.

License
-------

django-pymssql is released under the MIT license. See the LICENSE file.

Some database version checking code was borrowed from django-sqlserver_.

.. _almost: https://github.com/aaugustin/django-pymssql/blob/master/sqlserver_pymssql/known_django_test_failures.py
.. _django-mssql: http://django-mssql.readthedocs.org/
.. _django-pyodbc: https://github.com/lionheart/django-pyodbc/
.. _django-sqlserver: https://bitbucket.org/cramm/django-sqlserver
.. _pymssql: http://www.pymssql.org/
.. _pymssql.connect: http://pymssql.org/en/latest/ref/pymssql.html#pymssql.connect
.. _pyodbc: https://github.com/mkleehammer/pyodbc
.. _python-tds: https://github.com/denisenkom/pytds
