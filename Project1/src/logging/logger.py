import logging


def setup_logger(logger_name, log_file, level=logging.DEBUG):
    log = logging.getLogger(logger_name)
    formatter = logging.Formatter('[ %(asctime)s ] [ %(levelname)-5s ] %(message)s')
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    log.setLevel(level)
    log.addHandler(file_handler)
    log.addHandler(stream_handler)


setup_logger('employeeLog', r'employee.log')
employee_log = logging.getLogger('employeeLog')

setup_logger('managerLog', r'manager.log')
manager_log = logging.getLogger('managerLog')

setup_logger('reimbursementLog', r'reimbursement.log')
reimbursement_log = logging.getLogger('reimbursementLog')

setup_logger('loginLog', r'login.log')
login_log = logging.getLogger('loginLog')
