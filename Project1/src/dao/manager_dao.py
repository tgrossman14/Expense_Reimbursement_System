from src.utils.dbconfig import get_connection

# Get all managers
def get_all_managers():
    query_rows = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM "Project1".managers')
        query_rows = cursor.fetchall()
    finally:
        conn.close()
    return query_rows


# Get specific managers
def get_manager_by_id(manager_id):
    query_row = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM "Project1".managers WHERE manager_id={manager_id}')
        query_row = cursor.fetchone()
    finally:
        conn.close()
    return query_row