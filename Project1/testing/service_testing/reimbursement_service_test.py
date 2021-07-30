import unittest
from unittest import mock, TestCase
from src.models.reimbursement import Reimbursement
from testing.dao_test import *
from src.service.reimbursement_service import reimbursement_extended, list_of_dicts, jsonify
from src.service.employee_service import employee_extended


class ReimbursementServiceTest(unittest.TestCase):

    def test_get_all_reimbursements(self):
        db_reimbursements = test_get_all_reimbursements()
        if db_reimbursements != '()':
            reimbursement_list = list_of_dicts(db_reimbursements)
            for reimbursement in reimbursement_list:
                reimbursement['_reimbursement_amount'] = '$' + format(reimbursement['_reimbursement_amount'], '.2f')
            self.assertEqual(jsonify(reimbursement_list), {0 : {'_reimbursement_id': 1, '_reimbursement_approval': 'pending', '_reimbursement_amount': '$100.00', '_reimbursement_reason': '2 liters hydrogen peroxide', '_owner_id': 1},
                                                            1 : {'_reimbursement_id': 2, '_reimbursement_approval': 'approved', '_reimbursement_amount': '$200.00', '_reimbursement_reason': '45 syringes', '_owner_id': 1}})
        else:
            False


    def test_get_all_reimbursements_by_employee_id(self):
        u_exists = employee_extended(1)
        if u_exists:
            db_reimbursements = test_get_all_reimbursements_by_employee_id(1)
            if db_reimbursements != '()':
                reimbursement_list = list_of_dicts(db_reimbursements)
                self.assertEqual(jsonify(reimbursement_list), {0: {'_reimbursement_id': 1, '_reimbursement_approval': 'pending', '_reimbursement_amount': 100.0, '_reimbursement_reason': '2 liters hydrogen peroxide', '_owner_id': 1},
                                                            1: {'_reimbursement_id': 2, '_reimbursement_approval': 'approved', '_reimbursement_amount': 200.0, '_reimbursement_reason': '45 syringes', '_owner_id': 1}})
        else:
            False


    def test_calculate_statistics(self):
        reimbursements_amounts = test_get_all_reimbursement_amounts()
        reimbursement_approved_count = test_get_reimbursement_count()
        reimbursement_total_count = test_get_reimbursement_approved_count()
        reimbursement_approved_amounts = test_get_reimbursement_approved_amounts()
        
        if reimbursements_amounts != '()':
            reimbursement_total_sum = 0
            reimbursement_approved_sum = 0
            for amount in reimbursements_amounts:
                reimbursement_total_sum += amount.reimbursement_amount
            for amount in reimbursement_approved_amounts:
                reimbursement_approved_sum += amount.reimbursement_amount
            average = (reimbursement_total_sum / reimbursement_total_count[0])
            rate = (reimbursement_total_count[0] / reimbursement_approved_count[0]) * 100
            highest = max(reimbursements_amounts)
            approved_average = (reimbursement_approved_sum / reimbursement_approved_count[0])
            average = '$' + format(average, '.2f')
            rate = format(rate, '.2f') + '%'
            highest = '$' + format(highest[0], '.2f')
            approved_average = '$' + format(approved_average, '.2f')
            stats = {'average': average, 'rate': rate, 'highest': highest, 'approved_average': approved_average}
            self.assertEqual(stats, {'average': '$300.00', 'rate': '50.00%', 'highest': '$200.00', 'approved_average': '$100.00'})
        else:
            return False
