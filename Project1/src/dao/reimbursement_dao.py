from src.utils.dbconfig import get_connection


# Post new reimbursement
def post_new_reimbursement(reimbursement_amount, reimbursement_reason, owner_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO "Project1".reimbursements (reimbursement_approval, reimbursement_amount, reimbursement_reason, owner_id) values (\'pending\', {reimbursement_amount}, \'{reimbursement_reason}\', {owner_id})')
        conn.commit()
    finally:
        conn.close()


# Get reimbursement count
def get_reimbursement_count():
    query_row = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT Count (*) FROM "Project1".reimbursements')
        query_rows = cursor.fetchone()
    finally:
        conn.close()
    return query_rows


# Get all reimbursements
def get_all_reimbursements():
    query_rows = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM "Project1".reimbursements')
        query_rows = cursor.fetchall()
    finally:
        conn.close()
    return query_rows


# Get all reimbursements for single employee
def get_all_reimbursements_by_employee_id(employee_id):
    query_rows = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM "Project1".reimbursements WHERE owner_id={employee_id}')
        query_rows = cursor.fetchall()
    finally:
        conn.close()
    return query_rows


# Get specific reimbursement
def get_by_id(reimbursement_id):
    query_row = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM "Project1".reimbursements WHERE reimbursement_id=({reimbursement_id})')
        query_row = cursor.fetchone()
    finally:
        conn.close()
    return query_row


# Get all reimbursement amounts
def get_all_reimbursement_amounts():
    query_rows = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT reimbursement_amount FROM "Project1".reimbursements')
        query_rows = cursor.fetchall()
    finally:
        conn.close()
    return query_rows


# Update reimbursement amount
def patch_reimbursement_amount(reimbursement_id, new_amount):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f'UPDATE "Project1".reimbursements SET reimbursement_amount={new_amount} WHERE reimbursement_id={reimbursement_id}')
        conn.commit()
    finally:
        conn.close()


# Get reimbursement approved count
def get_reimbursement_approved_count():
    query_row = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f'SELECT COUNT (*) FROM "Project1".reimbursements WHERE reimbursement_approval=\'approved\'')
        query_row = cursor.fetchone()
    finally:
        conn.close()
    return query_row


# Get reimbursement approved amounts
def get_reimbursement_approved_amounts():
    query_rows = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT reimbursement_amount FROM "Project1".reimbursements WHERE reimbursement_approval=\'approved\'')
        query_rows = cursor.fetchall()
    finally:
        conn.close()
    return query_rows


# Update reimbursement approval
def patch_reimbursement_approval(reimbursement_id, new_approval):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f'UPDATE "Project1".reimbursements SET reimbursement_approval=\'{new_approval}\' WHERE reimbursement_id={reimbursement_id}')
        conn.commit()
    finally:
        conn.close()
