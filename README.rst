django-pymssql
==============

Goals
-----

django-pymssql is a Django database backend for Microsoft SQL Server that
works on non-Windows systems.

It's a small wrapper around django-mssql_ that uses pymssql_ instead of ADO
libraries.

It should support the same versions of Python, Django and SQL Server as
django-mssql_.

Unlike django-sqlserver_, it isn't a fork of django-mssql_, which should make
maintenance easier.

.. _django-mssql: http://django-mssql.readthedocs.org/
.. _pymssql: http://www.pymssql.org/
.. _django-sqlserver: https://bitbucket.org/cramm/django-sqlserver

License
-------

django-pymssql is released under the MIT license. See the LICENSE file.

Parts of the code were borrowed from django-sqlserver_.
