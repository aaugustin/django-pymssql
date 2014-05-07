import pymssql as Database

from sqlserver_ado.base import DatabaseWrapper as _DatabaseWrapper


DatabaseError = Database.DatabaseError
IntegrityError = Database.IntegrityError

VERSION_SQL2000 = 8
VERSION_SQL2005 = 9
VERSION_SQL2008 = 10


class CursorWrapper(object):

    def __init__(self, cursor):
        self.cursor = cursor

    def execute(self, query, args=None):
        if args is not None and not isinstance(args, tuple):
            args = tuple(args)
        if not isinstance(query, str):
            query = query.encode('utf-8')
        return self.cursor.execute(query, args)

    def __getattr__(self, attr):
        return getattr(self.cursor, attr)

    def __iter__(self):
        return iter(self.cursor)


class DatabaseWrapper(_DatabaseWrapper):

    Database = Database

    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)

    def get_connection_params(self):
        settings_dict = self.settings_dict
        return {
            'host': settings_dict['HOST'],
            'database': settings_dict['NAME'],
            'user': settings_dict['USER'],
            'password': settings_dict['PASSWORD'],
            'timeout': self.command_timeout,
        }

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
        Returns the 'DBMS Version' string, or ''. If a connection to the database has not already
        been established, a connection will be made when `make_connection` is True.
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
