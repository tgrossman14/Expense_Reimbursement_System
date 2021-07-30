import src.dao.reimbursement_dao as dao
from src.models.reimbursement import Reimbursement
from src.service.employee_service import employee_extended


def reimbursement_extended(reimbursement_id):
    exists = dao.get_by_id(reimbursement_id)
    if exists != '()':
        return exists
    else:
        return False


def list_of_dicts(db_reimbursements):
    reimbursement_list = []
    reimbursement_dict = {}
    for reimbursement in db_reimbursements:
        reimbursement = Reimbursement(reimbursement[0], reimbursement[1], reimbursement[2], reimbursement[3], reimbursement[4])
        for attr, value in reimbursement.__dict__.items():
            reimbursement_dict.update({attr: value})
        reimbursement_list.append(reimbursement_dict.copy())
    return reimbursement_list


def jsonify(reimbursements):
    reimbursement_dict = {}
    i = 0
    for reimbursement in reimbursements:
        reimbursement_dict.update({i: reimbursement})
        i += 1
    return reimbursement_dict


def get_all_reimbursements():
    db_reimbursements = dao.get_all_reimbursements()
    if db_reimbursements != '()':
        reimbursement_list = list_of_dicts(db_reimbursements)
        for reimbursement in reimbursement_list:
            reimbursement['_reimbursement_amount'] = '$' + format(reimbursement['_reimbursement_amount'], '.2f')
        return jsonify(reimbursement_list)
    else:
        return False


def get_all_reimbursements_by_employee_id(employee_id):
    u_exists = employee_extended(employee_id)
    if u_exists:
        db_reimbursements = dao.get_all_reimbursements_by_employee_id(employee_id)
        if db_reimbursements != '()':
            reimbursement_list = list_of_dicts(db_reimbursements)
            return jsonify(reimbursement_list)
    else:
        return False


def patch_reimbursement_approval(reimbursement_id, new_approval):
    exists = reimbursement_extended(reimbursement_id)
    if exists:
        dao.patch_reimbursement_approval(reimbursement_id, new_approval)
    else:
        return exists


def calculate_statistics():
    reimbursements_amounts = dao.get_all_reimbursement_amounts()
    reimbursement_approved_count = dao.get_reimbursement_count()
    reimbursement_total_count = dao.get_reimbursement_approved_count()
    reimbursement_approved_amounts = dao.get_reimbursement_approved_amounts()
    
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
        return stats
    else:
        return False
    


def post_new_reimbursement(reimbursement_amount, reimbursement_reason, employee_id):
    dao.post_new_reimbursement(reimbursement_amount, reimbursement_reason, employee_id)
