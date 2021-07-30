from flask.helpers import url_for
from flask.templating import render_template
from src.app import flask_app
from flask import request, make_response, redirect, session
import src.service.employee_service as es
import src.service.reimbursement_service as rs
from src.logging.logger import manager_log as log


@flask_app.route('/reimbursement_statistics/calculate')
def get_statistics():
    if "_manager_id" in session:
        json = rs.calculate_statistics()
        if json:
            log.info("Sending statistics...")
            return make_response(json, 200)
    else:
        return redirect(url_for("login"))


@flask_app.route('/manager_dashboard/reimbursement', methods=['GET'])
def get_all_reimbursements():
    if "_manager_id" in session:
        json = rs.get_all_reimbursements()
        if json:
            log.info("All reimbursements retrieved")
            return make_response(json, 200)
        else:
            log.error("No reimbursements found")
            return make_response("No reimbursements found", 404)
    else:
        return redirect(url_for("login"))


@flask_app.route('/manager_dashboard/all_employee', methods=['GET'])
def get_all_employees():
    json = es.get_all_employees()
    if json:
        log.info("All employees retrieved")
        return make_response(json, 200)
    else:
        log.error("No employees found")
        return make_response("No employees found", 404)


@flask_app.route('/manager_dashboard/employee/reimbursement', methods=['GET'])
def get_all_reimbursements_by_employee_id(employee_id):
    if "_manager_id" in session:
        json = rs.get_all_reimbursements_by_employee_id(employee_id)
        if json:
            log.info(f"All reimbursements retrieved for employee no. {employee_id}")
            return make_response(json, 200)
        else:
            log.error("No reimbursements found")
            return make_response("No reimbursements found", 404)
    else:
        return redirect(url_for("login"))


@flask_app.route('/manager_dashboard/reimbursement/approval', methods=['POST'])
def patch_reimbursement_approval():
    if "_manager_id" in session:
        client_json = request.get_json()
        for reimbursement in client_json:
            json = rs.patch_reimbursement_approval(reimbursement['reimbursement_id'], reimbursement['approval'])
            if json:
                log.info(f"Changing Reimbursement no. {reimbursement['reimbursement_id']} to {reimbursement['new_approval']}")
            else:
                log.error(f"Reimbursement no. {reimbursement['reimbursement_id']} not found")
                make_response(f"Reimbursement no. {reimbursement['reimbursement_id']} not found", 404)
        return redirect(url_for("manager_dashboard"))
    else:
        return redirect(url_for("login"))


@flask_app.route('/reimbursement_statistics')
def manager_statistics():
    if "_manager_id" in session:
        make_response("Accessing statistics page...", 200)
        return render_template('reimbursement_statistics.html')
    else:
        return redirect(url_for("login"))
