import unittest
from unittest import mock, TestCase
from src.models.manager import Manager
from testing.dao_test import test_get_all_managers
from src.service import manager_service as ms


class ManagerServiceTest(unittest.TestCase):
    
    def test_get_all_managers(self):
        db_managers = test_get_all_managers()
        if db_managers != '[]':
            manager_list = []
            manager_dict = {}
            for manager in db_managers:
                manager = Manager(manager[0], manager[1], manager[2])
                for attr, value in manager.__dict__.items():
                    manager_dict.update({attr: value})
                manager_list.append(manager_dict.copy())
            self.assertEqual(manager_list, [{'_manager_id': 1, '_manager_email': 'spotter@mash.gov', '_manager_password': 'horse'}, {'_manager_id': 2, '_manager_email': 'hblake@mash.gov', '_manager_password': 'fishing'}])
        else:
            return False
