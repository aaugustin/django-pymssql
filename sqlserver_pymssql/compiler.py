from sqlserver_ado.compiler import *                                    # noqa


# Replace the whole SQLUpdateCompiler with another implementation.

class SQLUpdateCompiler(compiler.SQLUpdateCompiler, SQLCompiler):

    def execute_sql(self, result_type):
        # Use a straight pymssql cursor to avoid throwing query counts off.
        # (Check Django's update_only_fields tests if you change this.)
        cursor = self.connection.connection.cursor()
        try:
            cursor.execute('SET NOCOUNT OFF')
            result = super(SQLUpdateCompiler, self).execute_sql(result_type)
            cursor.execute('SET NOCOUNT ON')
            return result
        finally:
            cursor.close()
