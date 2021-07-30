import unittest
from unittest import mock, TestCase
from src.models.employee import Employee
from testing.dao_test import TestDao as dao_test
from testing.dao_test import test_get_employee_by_id, test_get_all_employees


class EmployeeServiceTest(unittest.TestCase):

    def test_employee_extended(self):
        exists = test_get_employee_by_id(1)
        if exists != '{}':
            self.assertEqual(tuple(exists), (1, 'hpierce@mash.gov', 'crabapple', 'Hawkeye Pierce'))
        else:
            return False

    def test_get_all_employees(self):
        db_employees = test_get_all_employees()
        if db_employees != '[]':
            employee_list = []
            employee_dict = {}
            for employee in db_employees:
                employee = Employee(employee[0], employee[1], employee[2], employee[3])
                for attr, value in employee.__dict__.items():
                    employee_dict.update({attr:value})
                employee_list.append(employee_dict.copy())
            return self.assertEqual(employee_list, [{'_employee_id': 1, '_employee_email': 'hpierce@mash.gov', '_employee_password': 'crabapple', '_employee_fullname': 'Hawkeye Pierce'}, {'_employee_id': 2,'_employee_email': 'bhunnicut@mash.gov', '_employee_password': 'emily', '_employee_fullname': 'BJ Hunnicut'},{'_employee_id': 3, '_employee_email': 'mklinger@mash.gov', '_employee_password': 'shoes', '_employee_fullname': 'Maxwell Klinger'}])
        else:
            return self.assertEqual(db_employees, False)
