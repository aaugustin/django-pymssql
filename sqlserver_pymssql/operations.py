from sqlserver_ado.base import DatabaseOperations as _DatabaseOperations


class DatabaseOperations(_DatabaseOperations):
    compiler_module = "sqlserver_pymssql.compiler"
