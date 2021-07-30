import src.dao.employee_dao as dao
from src.models.employee import Employee


def employee_extended(employee_id):
    exists = dao.get_employee_by_id(employee_id)
    if exists != '{}':
        return exists
    else:
        return False


def get_all_employees():
    db_employees = dao.get_all_employees()
    if db_employees != '[]':
        employee_list = []
        employee_dict = {}
        for employee in db_employees:
            employee = Employee(employee[0], employee[1], employee[2], employee[3])
            for attr, value in employee.__dict__.items():
                employee_dict.update({attr:value})
            employee_list.append(employee_dict.copy())
        return employee_list
    else:
        return False
