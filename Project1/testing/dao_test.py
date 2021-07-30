from testing.dbconfig_test import testDBConfig
import unittest
from unittest import mock, TestCase


class TestDao(unittest.TestCase):

    def test_get_all_employees(self):
        query_rows = None
        try:
            conn = testDBConfig()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM test_employees')
            query_rows = cursor.fetchall()
        finally:
            conn.close()
        self.assertEqual(str(query_rows), str([(1, 'hpierce@mash.gov', 'crabapple', 'Hawkeye Pierce'),
                                     (2, 'bhunnicut@mash.gov', 'emily', 'BJ Hunnicut'),
                                     (3, 'mklinger@mash.gov', 'shoes', 'Maxwell Klinger')]))
        return query_rows

    def test_get_employee_by_id(self):
        query_row = None
        try:
            employee_id = 1
            conn = testDBConfig()
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM test_employees WHERE employee_id={employee_id}')
            query_row = cursor.fetchone()
        finally:
            conn.close()
        self.assertEqual(str(query_row), str((1, 'hpierce@mash.gov', 'crabapple', 'Hawkeye Pierce')))
        return query_row

    def test_get_all_managers(self):
        query_rows = None
        try:
            conn = testDBConfig()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM test_managers')
            query_rows = cursor.fetchall()
        finally:
            conn.close()
        self.assertEqual(str(query_rows), str([(1, 'spotter@mash.gov', 'horse'), (2, 'hblake@mash.gov', 'fishing')]))
        return query_rows

    def test_get_manager_by_id(self):
        query_row = None
        try:
            manager_id = 1
            conn = testDBConfig()
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM test_managers WHERE manager_id={manager_id}')
            query_row = cursor.fetchone()
        finally:
            conn.close()
        self.assertEqual(str(query_row), str((1, 'spotter@mash.gov', 'horse')))
        return query_row

    # Get reimbursement count
    def test_get_reimbursement_count(self):
        query_row = None
        try:
            conn = testDBConfig()
            cursor = conn.cursor()
            cursor.execute('SELECT Count (*) FROM test_reimbursements')
            query_rows = cursor.fetchone()
        finally:
            conn.close()
        self.assertEqual(str(query_rows), '(2, )')
        return query_rows

    # Get all reimbursements
    def test_get_all_reimbursements(self):
        query_rows = None
        try:
            conn = testDBConfig()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM test_reimbursements')
            query_rows = cursor.fetchall()
        finally:
            conn.close()
        self.assertEqual(str(query_rows), str([(1, 'pending', 100.0, '2 liters hydrogen peroxide', 1),
                                        (2, 'approved', 200.0, '45 syringes', 1)]))
        return query_rows

    # Get all reimbursement amounts
    def test_get_all_reimbursement_amounts(self):
        query_rows = None
        try:
            conn = testDBConfig()
            cursor = conn.cursor()
            cursor.execute('SELECT reimbursement_amount FROM test_reimbursements')
            query_rows = cursor.fetchall()
        finally:
            conn.close()
        self.assertEqual(str(query_rows), '[(100.0, ), (200.0, )]')
        return query_rows

    # Get reimbursement approved count
    def test_get_reimbursement_approved_count(self):
        query_row = None
        try:
            conn = testDBConfig()
            cursor = conn.cursor()
            cursor.execute(f'SELECT COUNT (*) FROM test_reimbursements WHERE reimbursement_approval=\'approved\'')
            query_row = cursor.fetchone()
        finally:
            conn.close()
        self.assertEqual(str(query_row), '(1, )')
        return query_row

    # Get reimbursement approved amounts
    def test_get_reimbursement_approved_amounts(self):
        query_rows = None
        try:
            conn = testDBConfig()
            cursor = conn.cursor()
            cursor.execute('SELECT reimbursement_amount FROM test_reimbursements WHERE reimbursement_approval=\'approved\'')
            query_rows = cursor.fetchall()
        finally:
            conn.close()
        self.assertEqual(str(query_rows), '[(200.0, )]')
        return query_rows


def test_get_all_managers():
    query_rows = None
    try:
        conn = testDBConfig()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM test_managers')
        query_rows = cursor.fetchall()
    finally:
        conn.close()
    return query_rows

def test_get_all_employees():
    query_rows = None
    try:
        conn = testDBConfig()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM test_employees')
        query_rows = cursor.fetchall()
    finally:
        conn.close()
    return query_rows


def test_get_employee_by_id(employee_id):
    query_row = None
    try:
        conn = testDBConfig()
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM test_employees WHERE employee_id={employee_id}')
        query_row = cursor.fetchone()
    finally:
        conn.close()
    return query_row


def test_get_manager_by_id(manager_id):
    query_row = None
    try:
        conn = testDBConfig()
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM test_managers WHERE manager_id={manager_id}')
        query_row = cursor.fetchone()
    finally:
        conn.close()
    return query_row


def test_get_all_reimbursements_by_employee_id(employee_id):
    query_rows = None
    try:
        conn = testDBConfig()
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM test_reimbursements WHERE owner_id={employee_id}')
        query_rows = cursor.fetchall()
    finally:
        conn.close()
    return query_rows


def test_get_by_id(reimbursement_id):
    query_row = None
    try:
        conn = testDBConfig()
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM test_reimbursements WHERE reimbursement_id=({reimbursement_id})')
        query_row = cursor.fetchone()
    finally:
        conn.close()
    return query_row


def test_get_all_reimbursement_amounts():
    query_rows = None
    try:
        conn = testDBConfig()
        cursor = conn.cursor()
        cursor.execute('SELECT reimbursement_amount FROM test_reimbursements')
        query_rows = cursor.fetchall()
    finally:
        conn.close()
    return query_rows

def test_get_all_reimbursements():
    query_rows = None
    try:
        conn = testDBConfig()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM test_reimbursements')
        query_rows = cursor.fetchall()
    finally:
        conn.close()
    return query_rows


def test_get_reimbursement_count():
    query_row = None
    try:
        conn = testDBConfig()
        cursor = conn.cursor()
        cursor.execute('SELECT Count (*) FROM test_reimbursements')
        query_rows = cursor.fetchone()
    finally:
        conn.close()
    return query_rows



# Get reimbursement approved count
def test_get_reimbursement_approved_count():
    query_row = None
    try:
        conn = testDBConfig()
        cursor = conn.cursor()
        cursor.execute(f'SELECT COUNT (*) FROM test_reimbursements WHERE reimbursement_approval=\'approved\'')
        query_row = cursor.fetchone()
    finally:
        conn.close()
    return query_row


def test_get_reimbursement_approved_amounts():
    query_rows = None
    try:
        conn = testDBConfig()
        cursor = conn.cursor()
        cursor.execute('SELECT reimbursement_amount FROM test_reimbursements WHERE reimbursement_approval=\'approved\'')
        query_rows = cursor.fetchall()
    finally:
        conn.close()
    return query_rows
