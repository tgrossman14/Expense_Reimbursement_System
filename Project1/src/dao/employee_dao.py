from src.utils.dbconfig import get_connection

# Get all employees
def get_all_employees():
    query_rows = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM "Project1".employees')
        query_rows = cursor.fetchall()
    finally:
        conn.close()
    return query_rows


# Get specific employees
def get_employee_by_id(employee_id):
    query_row = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM "Project1".employees WHERE employee_id={employee_id}')
        query_row = cursor.fetchone()
    finally:
        conn.close()
    return query_row