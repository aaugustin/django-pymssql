import datetime

from django.utils import timezone

import pymssql as Database

from sqlserver_ado.base import (
    DatabaseFeatures as _DatabaseFeatures,
    DatabaseOperations as _DatabaseOperations,
    DatabaseWrapper as _DatabaseWrapper)

DatabaseError = Database.DatabaseError
IntegrityError = Database.IntegrityError

VERSION_SQL2000 = 8
VERSION_SQL2005 = 9
VERSION_SQL2008 = 10


def _fix_query(query):
    # For Django's inspectdb tests -- a model has a non-ASCII column name.
    if not isinstance(query, str):
        query = query.encode('utf-8')
    # For Django's backends and expressions_regress tests.
    query = query.replace('%%', '%')
    return query


def _fix_value(value):
    if isinstance(value, datetime.datetime):
        if timezone.is_aware(value):
            value = timezone.make_naive(value, timezone.utc)
    return value


def _fix_params(params):
    if params is not None:
        # pymssql needs a tuple, not another kind of iterable.
        params = tuple(_fix_value(value) for value in params)
    return params


class CursorWrapper(object):

    def __init__(self, cursor):
        self.cursor = cursor

    def callproc(self, procname, params=None):
        params = _fix_params(params)
        return self.cursor.callproc(procname, params)

    def execute(self, query, params=None):
        query = _fix_query(query)
        params = _fix_params(params)
        return self.cursor.execute(query, params)

    def executemany(self, query, param_list):
        query = _fix_query(query)
        param_list = [_fix_params(params) for params in param_list]
        return self.cursor.executemany(query, param_list)

    def __getattr__(self, attr):
        return getattr(self.cursor, attr)

    def __iter__(self):
        return iter(self.cursor)


class DatabaseOperations(_DatabaseOperations):

    compiler_module = "sqlserver_pymssql.compiler"


class DatabaseFeatures(_DatabaseFeatures):

    can_introspect_max_length = False
    can_introspect_null = False
    can_introspect_decimal_field = False

    failing_tests = _DatabaseFeatures.failing_tests.copy()
    failing_tests.update({

        # pymssql doesn't handle binary data correctly.
        'backends.tests.LastExecutedQueryTest'
        '.test_query_encoding': [(1, 7)],
        'model_fields.tests.BinaryFieldTests'
        '.test_set_and_retrieve': [(1, 7)],

        # pymssql doesn't check parameter counts.
        'backends.tests.ParameterHandlingTest'
        '.test_bad_parameter_count': [(1, 7)],

        # Several tests that depend on schema alteration fail at this time.
        # This should get fixed in django-mssql when it supports migrations.

    })


class DatabaseWrapper(_DatabaseWrapper):

    Database = Database

    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        self.features = DatabaseFeatures(self)
        self.ops = DatabaseOperations(self)

    def get_connection_params(self):
        settings_dict = self.settings_dict
        params = {
            'host': settings_dict['HOST'],
            'database': settings_dict['NAME'],
            'user': settings_dict['USER'],
            'password': settings_dict['PASSWORD'],
            'port': settings_dict['PORT'],
        }
        options = settings_dict.get('OPTIONS', {})
        params.update(options)
        return params

    def get_new_connection(self, conn_params):
        return Database.connect(**conn_params)

    def init_connection_state(self):
        # Not calling super() because we don't care much about version checks.
        pass

    def create_cursor(self):
        cursor = self.connection.cursor()
        return CursorWrapper(cursor)

    def _set_autocommit(self, autocommit):
        self.connection.autocommit(autocommit)

    def __get_dbms_version(self, make_connection=True):
        """
        Returns the 'DBMS Version' string, or ''. If a connection to the
        database has not already been established, a connection will be made
        when `make_connection` is True.
        """
        if not self.connection and make_connection:
            self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT SERVERPROPERTY('productversion')")
            return cursor.fetchone()[0]

    def _is_sql2005_and_up(self, conn):
        return self._get_major_ver(conn) >= VERSION_SQL2005

    def _is_sql2008_and_up(self, conn):
        return self._get_major_ver(conn) >= VERSION_SQL2008
