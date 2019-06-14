"""
Set of SQLAlchemy database schemas supported in MLflow for tracking server backends.
"""

POSTGRES = 'postgresql'
MYSQL = 'mysql'
MYSQL2 = 'mysql+pymysql'
SQLITE = 'sqlite'
MSSQL = 'mssql'

DATABASE_ENGINES = [
    POSTGRES,
    MYSQL,
    MYSQL2,
    SQLITE,
    MSSQL
]
