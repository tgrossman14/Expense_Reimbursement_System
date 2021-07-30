import src.dao.manager_dao as dao
from src.models.manager import Manager

def get_all_managers():
    db_managers = dao.get_all_managers()
    if db_managers != '[]':
        manager_list = []
        manager_dict = {}
        for manager in db_managers:
            manager = Manager(manager[0], manager[1], manager[2])
            for attr, value in manager.__dict__.items():
                manager_dict.update({attr:value})
            manager_list.append(manager_dict.copy())
        return manager_list
    else:
        return False
