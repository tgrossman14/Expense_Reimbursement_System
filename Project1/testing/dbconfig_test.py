import os
import pyodbc


def testDBConfig():

    conn = pyodbc.connect("DRIVER=PostgreSQL UNICODE(x64); SERVER=localhost; PORT=5432; DATABASE=postgres; "
                           "UID=postgres; PWD=postgres")
    return conn
