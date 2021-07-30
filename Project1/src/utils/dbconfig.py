from pyodbc import connect
import os

db_url = os.environ['db_url']
db_username = os.environ['db_username']
db_password = os.environ['db_password']
db_name = os.environ['db_name']


def get_connection():
    return connect(f"DRIVER={{PostgreSQL UNICODE(x64)}};SERVER={db_url};PORT=5432;DATABASE={db_name};UID={db_name};PWD={db_password};Trusted_Connection=no")
