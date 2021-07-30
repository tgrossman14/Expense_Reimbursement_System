from flask.helpers import url_for
from src.app import flask_app
from flask import request, make_response, redirect, render_template, session
import src.service.employee_service as es
import src.service.manager_service as ms
from src.logging.logger import login_log as log


# Takes in form data
@flask_app.route('/login', methods=['POST'])
def login():
    # Form input only accessed by its "name" attribute
    # request.args.get works for GET .. request.form.get works for POST
    email = request.form.get('email')
    password = request.form.get('password')
    log.info(email)
    log.info(password)
    employees = es.get_all_employees()
    managers = ms.get_all_managers()
    employee_info_dict = {}
    manager_info_dict = {}
    for manager in managers:
        manager_info_dict.update({manager['_manager_email']: manager['_manager_password'], '_manager_id': manager['_manager_id']})
    for employee in employees:
        employee_info_dict.update({employee['_employee_email']: employee['_employee_password'], '_employee_id': employee['_employee_id']})
    if email in employee_info_dict:
        if password == employee_info_dict[f'{email}']:
            session['_employee_id'] = employee_info_dict['_employee_id']
            make_response("Logging in...", 200)
            return redirect(url_for("employee_dashboard"))
        else:
            return render_template("login.html")
    elif email in manager_info_dict:
        if password == manager_info_dict[f'{email}']:
            session['_manager_id'] = manager_info_dict['_manager_id']
            make_response("Logging in...", 200)
            return redirect(url_for("manager_dashboard"))
        else:
            return render_template("login.html")
    else:
        make_response("Invalid credentials", 404)
        return render_template("login.html")


@flask_app.route('/employee_dashboard')
def employee_dashboard():
    if "_employee_id" in session:
        make_response("Logging in...", 200)
        return render_template("employee_dashboard.html")
    else:
        return redirect(url_for("login"))


@flask_app.route('/manager_dashboard')
def manager_dashboard():
    if "_manager_id" in session:
        make_response("Logging in...", 200)
        return render_template('manager_dashboard.html')
    else:
        return redirect(url_for("login"))


@flask_app.route("/logout")
def logout():
    log.info("Logging out")
    if "_manager_id" in session:
        session.pop("_manager_id", None)
    else:
        session.pop("_employee_id", None)
    return redirect(url_for("login"))
